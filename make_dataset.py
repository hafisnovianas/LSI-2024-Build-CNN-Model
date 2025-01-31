import os
import module.utility as utility

dataName = 'OPLOSAN'
sourceFolderPath = os.path.join('data\source_data\DATA PROTOTIPE', dataName)
latihFolderPath = os.path.join('data\dataset\data_latih',dataName)
ujiFolderPath = os.path.join('data\dataset\data_uji',dataName)

os.makedirs(latihFolderPath, exist_ok=True)
os.makedirs(ujiFolderPath, exist_ok=True)

for itemName in os.listdir(sourceFolderPath):
    itemPath = os.path.join(sourceFolderPath,itemName)
    
    latihSourceFolderPath = os.path.join(itemPath, itemName + '(data latih)')
    utility.copyAllFile(latihSourceFolderPath, latihFolderPath)

    ujiSourceFolderPath = os.path.join(itemPath, itemName + '(data uji)')
    utility.copyAllFile(ujiSourceFolderPath, ujiFolderPath)