import pickle

class animClass:
    def __init__(self,id=None,name=None,name_rus=None,hex_name=None,poster=None,screenshot=None,anime_score=None,user_score=None,description=None,kind=None,franchise=None):
        self.id=id
        self.name=name
        self.hex_name=hex_name
        self.name_rus=name_rus
        self.poster=poster
        self.screenshot=screenshot
        self.anime_score=anime_score
        self.user_score=user_score
        self.description=description
        self.kind=kind
        self.franchise=franchise
        self.genres=[]

file=open('anime_dict10000.txt','rb')

anime_list=pickle.load(file)

file.close()





anime_dict={}
for id,anime in anime_list.items():
    anime_dict[int(id)]=anime


file=open('anime_dict10000_v2.txt','wb')
pickle.dump(anime_dict,file)
file.close()