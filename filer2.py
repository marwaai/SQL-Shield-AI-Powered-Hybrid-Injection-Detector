from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from main import lf
import polars as pl
from sklearn.pipeline import Pipeline
import joblib
# ... باقي الاستدعاءات

# 1. تجهيز البيانات من Polars كقوائم نصوص
df = lf.collect()
X_raw = df["Query"].to_list()
y = df["Label"].to_list()

# 2. إنشاء Pipeline يجمع بين تحويل النصوص والموديل
text_clf = Pipeline([
    ('tfidf', TfidfVectorizer(analyzer='char', ngram_range=(1, 3))),
    ('clf', RandomForestClassifier())
])

# 3. تقسيم البيانات (نمرر النصوص الخام هنا عادي)
X_train, X_test, y_train, y_test = train_test_split(X_raw, y, test_size=0.2)

# 4. التدريب (الـ Pipeline سيقوم بعمل fit_transform داخلياً)
text_clf.fit(X_train, y_train)

# 5. التقييم
predictions = text_clf.predict(X_test)
print(classification_report(y_test, predictions))
joblib.dump(text_clf, 'sql_detector_model.pkl')