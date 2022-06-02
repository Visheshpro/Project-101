import dropbox,os

accesstoken = "sl.BIn5pTnUakNAjNUOtkwtX0xj3H4aqfdt-pSorrvsGx4KBdwVAwF_BjcvGl1N1fuSDQ5U8ZXqzyGErYcgN2N6vIUhUudgEGbxs0j-JdciZKQuechEMCFuwAeEmo6Oq61kL36SIgCpnmII"

dbx = dropbox.Dropbox(accesstoken)

source = "D:/PROJECTS/Python/Class Works"
destination = "/projects/"

for root,folder,files in os.walk(source):
    for file in files:
        data = open(root+"/"+file,"rb").read()
        dbx.files_upload(data,destination+file)