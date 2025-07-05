from langdetect import detect
import re

def detect_language(text):
    """
    Detect English or Odia text using langdetect + Unicode heuristics.
    
    Args:
        text (str): Input text
    
    Returns:
        str: 'en' or 'or' or 'unknown'
    """
    
    odia_chars = re.findall(r'[\u0B00-\u0B7F]', text)
    if len(odia_chars) > 30:  
        return 'or'
    
    try:
        lang = detect(text)
        if lang == 'en':
            return 'en'
        else:
            return 'unknown'
    except:
        return 'unknown'

if __name__ == "__main__":
    english = "This is a book about Odia literature."
    odia = "ଏହା ଗୋଟିଏ ଓଡ଼ିଆ ସାହିତ୍ୟ ବିଷୟରେ ପୁସ୍ତକ ଅଟେ।"
    
    print(detect_language(english))  
    print(detect_language(odia))     