import boto3

def translate_text(source_text, target_languages):
    translations = {}
    
    for target_language in target_languages:
        translate = boto3.client('translate', region_name='us-east-1')  # Replace 'your-region' with your AWS region
        response = translate.translate_text(
            Text=source_text,
            SourceLanguageCode='auto',
            TargetLanguageCode=target_language
        )
        translations[target_language] = response['TranslatedText']
    
    return translations

def generate_audio(text, voice_id):
    polly = boto3.client('polly', region_name='us-east-1')  # Replace 'your-region' with your AWS region
    response = polly.synthesize_speech(
        Text=text,
        OutputFormat='mp3',
        VoiceId=voice_id
    )
    
    # Save the audio file
    with open('translated_audio.mp3', 'wb') as file:
        file.write(response['AudioStream'].read())

if __name__ == "__main__":
    source_text = input("Enter the text to translate: ")
    target_languages = ["ko", "zh"]  # Set target languages to Korean (ko) and Chinese (zh)
    valid_voice_id = "Matthew"  # Choose a valid voiceId from the error message list
    
    translations = translate_text(source_text, target_languages)
    
    for lang, translation in translations.items():
        print(f"\nTranslated Text ({lang}): {translation}")

    # Use the valid voiceId for audio generation
    generate_audio(translations[target_languages[-1]], valid_voice_id)
    print("Audio file 'translated_audio.mp3' generated.")
