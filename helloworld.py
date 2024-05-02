from docx import Document
def greet(lang):
    if lang=="es":
        return "holla"
    elif lang=="fr":
        return "Bonjour"
    else:
        return "Hello"
def congratulation_message(greet, name):
    return f'''{greet}, {name},
    we are pleased to inform you that your application for permanent residency status in canada has been approved.
kindly send in your passport for completion of the process. Please note that the proces of returning your passport
after stamp takes about 5 business days.
    Once again,congratulations {name} as only few persons gets this privilege in their life time.
with this I say welcome to canada {name}

Regards,
Marc Miller.
Immigration, Refugees and Citizenship Canada Minister.
'''


name=input("what is your name? ")
lang=input("what language do you prefer? ")
don= greet(lang)

doc = Document()
message=congratulation_message(don, name)
doc.add_paragraph(message)
doc.save("congratulatory_messageTessy.docx")





















