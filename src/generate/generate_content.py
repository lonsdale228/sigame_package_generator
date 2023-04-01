import os
import secrets
import xml.etree.ElementTree as ET
from src.entities.rounds import question,line


m_encoding = 'UTF-8'

package = ET.Element("package")
package.set("name","beba")
package.set("version","4")
id=secrets.token_hex(32)
package.set("id",id)
package.set("date","01.01.2001")
package.set("publisher","beba")
package.set("difficulty","5")
package.set("xmlns","http://vladimirkhil.com/ygpackage3.0.xsd")

info=ET.SubElement(package,"info")

authors=ET.SubElement(info,"authors")
author=ET.SubElement(authors,"author").text="_"
comments=ET.SubElement(info,"comments").text="_"

rounds=ET.SubElement(package,"rounds")

numOfQuestions=300
rounds_num=numOfQuestions//100
for i in range(rounds_num):
    round=ET.SubElement(rounds,"round")
    themes=ET.SubElement(round,"themes")










def create_screenshot_line(animes,limit=15):

    temp_line = line()
    temp_line.questions = []

    for i in range(limit):
        temp_question = question()
        temp_question.price = 100
        temp_question.type = "image"
        try:
            if animes[0].screenshot!=None:
                temp_question.answer = animes[0].name + " / " + animes[0].name_rus
                temp_question.hex = animes[0].hex_name
                temp_line.questions.append(temp_question)
            animes.pop(0)

        except IndexError:
            ...

        if len(animes) == 0: return temp_line
    return temp_line


def create_audio_line(animes,limit=15,start=1):

    temp_line = line()
    temp_line.questions=[]

    for i in range(limit):
        temp_question = question()
        temp_question.price = 100
        temp_question.type = "voice"
        try:
            temp_question.answer=animes[0].name+" / "+animes[0].name_rus
            temp_question.hex=animes[0].hex_name

            temp_line.questions.append(temp_question)

            animes.pop(0)
        except IndexError:
            ...

        if len(animes)==0: return temp_line
    return temp_line

def create_scr_round(animes,limit=10):
    from src.entities.rounds import round
    temp_round=round()
    temp_round.lines=[]

    for i in range(limit):
        temp_round.lines.append(create_screenshot_line(animes))
        temp_round.lines[i].name=f"Screenshot {i+1}"
    return temp_round


def create_round(animes,limit=10):
    from src.entities.rounds import round
    temp_round=round()
    temp_round.lines=[]

    for i in range(limit):
        temp_round.lines.append(create_audio_line(animes))
        temp_round.lines[i].name=f"OP {i+1}"
    return temp_round


def create_xml_round(round,type):
    xml_round=ET.Element("round",name=round.name)
    xml_themes=ET.SubElement(xml_round,"themes")
    for line in round.lines:
        xml_line=ET.SubElement(xml_themes,"theme",name=line.name)
        xml_questions=ET.SubElement(xml_line,"questions")
        for question in line.questions:
            xml_que=ET.SubElement(xml_questions,"question",price=f"{question.price}")
            xml_scenario=ET.SubElement(xml_que,"scenario")
            xml_atom_type=ET.SubElement(xml_scenario,"atom",type=f"{question.type}")
            match type:
                case "audio":
                    xml_atom_type.text="@"+question.hex+".m4a"
                case "image":
                    xml_atom_type.text = "@" + question.hex + ".jpg"
                case "video":
                    xml_atom_type.text = "@" + question.hex + ".mp4"
            xml_right=ET.SubElement(xml_que,"right")
            xml_answer=ET.SubElement(xml_right,"answer")
            xml_answer.text=question.answer
    return xml_round


def create_xml(xml_round):
    package_name="Test"
    package_id=secrets.token_hex(16)
    root = ET.Element("package", {
        "name": package_name,
        "version": "4",
        "id": f"{package_id}",
        "date": "01.01.2023",
        "publisher": "lonsdale",
        "difficulty": "5",
        "xmlns": "http://vladimirkhil.com/ygpackage3.0.xsd"
    })
    rounds = ET.SubElement(root, "rounds")
    rounds.append(xml_round)
    tree = ET.ElementTree(root)
    tree.write("temp\\"+"content.xml", encoding="utf-8", xml_declaration=True)






print(ET.dump(package))
