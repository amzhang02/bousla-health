from googleapiclient import discovery
import json

API_KEY = 'AIzaSyAoQqGKdy5yPj9GXFy5fxl2C5spYXVvahE'

client = discovery.build(
  "commentanalyzer",
  "v1alpha1",
  developerKey=API_KEY,
  discoveryServiceUrl="https://commentanalyzer.googleapis.com/$discovery/rest?version=v1alpha1",
  static_discovery=False,
)

def mod(comment):
    analyze_request = {
    'comment': { 'text': comment },
    'requestedAttributes': {'TOXICITY': {},'IDENTITY_ATTACK': {}, 'INSULT': {}, 'THREAT':{}, 'OBSCENE': {} }
    }
    try:
        response = client.comments().analyze(body=analyze_request).execute()
    except Exception as e:
    # Handle the exception here if needed
        return False
    # Check if any attribute score is greater than 0.8
    attributes = [
        'TOXICITY',
        'IDENTITY_ATTACK',
        'INSULT',
        'THREAT',
        'OBSCENE'
    ]
    is_greater_than_08 = any(
        response.get('attributeScores', {}).get(attr, {}).get('summaryScore', {}).get('value', 0) > 0.8
        for attr in attributes
    )

    # Set a value to true if any attribute score is greater than 0.8
    return is_greater_than_08
