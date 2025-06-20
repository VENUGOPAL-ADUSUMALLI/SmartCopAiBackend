
from users.utils.ai_predictor import get_ai_assessment
incident_summary = """
On June 15th, a 25-year-old woman was followed by two men in a dark alley while returning from work. 
They passed lewd comments, tried to grab her bag, and blocked her path. 
She screamed and ran into a nearby store. CCTV footage captured the incident. 
She filed a police complaint and gave a detailed statement.
"""

result = get_ai_assessment(incident_summary)

print("\n✅ FINAL RESULT FROM AI:")
print(result)
