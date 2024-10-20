import cv2
import os
import glob
from PIL import Image

# 1 - Tratando os captcha para facilitar o treinamento da IA

def tratar_imagem(pasta_origem, pasta_destino='captcha_tratado'):
  arquivos = glob.glob(f"{pasta_origem}/*")

  for arquivo in arquivos:
    imagem = cv2.imread(arquivo)

    # transformar a imagem em escala de cinza
    imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_RGB2GRAY)

    _, imagem_tratada = cv2.threshold(imagem_cinza, 127, 255, cv2.THRESH_TRUNC or cv2.THRESH_OTSU)
    nome_arquivo = os.path.basename(arquivo)
    cv2.imwrite(f'{pasta_destino}/{nome_arquivo}', imagem_tratada)

    arquivos = glob.glob(f"{pasta_destino}/*")
    for arquivo in arquivos:
      imagem = Image.open(arquivo)
      imagem = imagem.convert("L")
      #imagem = imagem.convert("P")  antes 
      imagem2 = Image.new("P", imagem.size, (255, 255, 255))
      #imagem2 = Image.new("P", imagem.size, 255)  antes

      for x in range(imagem.size[1]):
        for y in range(imagem.size[0]):
          cor_pixel = imagem.getpixel((y, x))
          if cor_pixel < 115:
            imagem2.putpixel((y, x), (0, 0, 0))
            #imagem2.putpixel((y, x), 0)  antes

      nome_arquivo = os.path.basename(arquivo)
      imagem2.save(f'{pasta_destino}/{nome_arquivo}')


if __name__ == "__main__":
  tratar_imagem('bd_captcha')
