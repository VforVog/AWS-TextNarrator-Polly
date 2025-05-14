import boto3

def lambda_handler(event, context):
    
    polly = boto3.client('polly')

    s3_bucket = 'vogapp-polly'
    s3_file = 'Polly-Project.txt'


    s3 = boto3.client('s3')
    text_object = s3.get_object(Bucket=s3_bucket, Key=s3_file)
    text_content = text_object['Body'].read().decode('utf-8')


    response = polly.synthesize_speech(
        Text=text_content,
        OutputFormat='mp3',
        VoiceId='Joanna'
    )
    
    audio_data = response['AudioStream'].read()
    s3.put_object(
        Bucket=s3_bucket, 
        Key='output.mp3', 
        Body=audio_data,
        ContentType='audio/mpeg')


    return {
        'statusCode' : 200,
        'body' : 'Polly Project Success'
    }
