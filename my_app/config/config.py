class Config:
    ACCESS_TOKEN = open("./user_token",'r').readlines()[0]
    SQLALCHEMY_DATABASE_URI = 'sqlite:///project.db'
    OPENAI_API_KEY = open("./env",'r').readlines()[0].strip("\n")
    