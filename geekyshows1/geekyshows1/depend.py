def main():
    print('DONE')

def lambda_handler(event, context):
    main()
    return "Hello Lambda"