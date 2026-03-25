from sqlglot import parse_one, errors
def is_valid_sql(text):
    # 1. حالة النص الفارغ
    if not text:
        return "Empty/Null" 

    try:
        parse_one(text)
        return "SQL Command"
        
    # 2. حالة الكلام البشري أو الخطأ في قواعد SQL
    except (errors.ParseError, errors.TokenError): 
        return "Human Talk" 

    # 3. حالة "الغرابة" أو الأخطاء التقنية (وهي نادرة جداً)
    except Exception:
        return "Processing Error"
print(is_valid_sql("------/*SELECT good product "))
print(is_valid_sql("SELECT * FROM users WHERE username = '' OR '1'='1' --';"))
print(is_valid_sql("SELECT * FROM users WHERE username = 'marwa';"))