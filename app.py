import streamlit as st
import joblib
import re
from filter1 import is_valid_sql

# --- 1. تحميل الموديل ---
@st.cache_resource
def load_model():
    try:
        return joblib.load('sql_detector_model.pkl')
    except Exception as e:
        st.error(f"خطأ في تحميل الموديل: {e}")
        return None

model = load_model()

# --- 2. دالة الفحص الأمني السريع (Regex Filter) ---
def security_scan(text):
    hex_pattern = r'0x[0-9a-fA-F]+'
    union_pattern = r'(?i)\bUNION\b.*\bSELECT\b'
    
    if re.search(hex_pattern, text):
        return "Hex Encoding Detected"
    if re.search(union_pattern, text):
        return "Union-based Injection Attempt"
    return None

# --- 3. واجهة التطبيق ---
st.set_page_config(page_title="SQL Shield", page_icon="🛡️")
st.title("🛡️ SQL Injection Hybrid Detector")
st.markdown("---")

query_input = st.text_area("أدخلي النص أو الاستعلام للاختبار:", placeholder="SELECT * FROM users أو أي نص عادي...")

if st.button("تحليل الآن"):
    if query_input:
        
        # --- المرحلة 0: الفحص الأمني السريع (الريجكس) ---
        scan_result = security_scan(query_input)
        if scan_result:
            st.error(f"🚨 حظر أمني فوري: {scan_result}!")
            st.warning("تم إيقاف الفحص. النص يحتوي على نمط اختراق صريح (Bypassed ML).")
            st.stop() # توقف هنا لأن الريجكس هو الأقوى في هذه الحالة
        
        # --- المرحلة 1: الفلتر التقليدي (تحديد نوع النص) ---
        # نستخدمه هنا كـ Gatekeeper لحماية الموديل من النصوص العادية
        is_sql = is_valid_sql(query_input)
        
        st.subheader("🔍 تفاصيل التحليل")
        
        if not is_sql:
            # إذا كان نصاً عادياً، لا نرسله للموديل
            st.info("ℹ️ الفلتر التقليدي: النص المدخل يبدو ككلام عادي وليس استعلام SQL صالح.")
            st.success("✅ النتيجة: نص آمن (تم تخطي فحص الذكاء الاصطناعي لمنع الأخطاء).")
        else:
            # --- المرحلة 2: فحص الذكاء الاصطناعي ---
            # الموديل يتدخل فقط لأننا تأكدنا أنه SQL
            st.info("ℹ️ الفلتر التقليدي: تم التعرف على النص كاستعلام SQL. جاري الفحص العميق...")
            
            if model:
                prediction = model.predict([query_input])[0]
                
                if prediction == 1:
                    st.error("🚨 نتيجة الذكاء الاصطناعي: تم اكتشاف SQL Injection!")
                else:
                    st.success("✅ نتيجة الذكاء الاصطناعي: استعلام SQL آمن.")
            else:
                st.warning("تعذر تشغيل الموديل الذكي.")

    else:
        st.info("الرجاء إدخال نص لبدء الفحص.")