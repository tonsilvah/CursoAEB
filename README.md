<!DOCTYPE html>
<html lang="pt-BR">
<body>
    <h1><b>Este jogo foi desenvolvido no curso de Programação de Jogos em Python - 2ª Turma/2024, ofertado pela AGENCIA ESPACIAL BRASILEIRA (AEB) ESCOLA </b></h1>
    <p><b> AEB ESCOLA VIRTUAL </b> https://aebescolavirtual.aeb.gov.br</p>
    <p>-----</p>
    <h1>DIAGRAMA DO JOGO</h1>
    <img src="Captura de tela 2024-09-25 204941.png")>
    <h1><b>CLASSES DO JOGO</b></h1>
    <p><b>GAME</b> - responsável pela lógica e início do jogo</p>
    <p><b>BACKGROUND</b> - responsável pela seleção do plano de fundo</p>
    <p><b>PLAYER</b> - responsável pela construção, posicionamento e imagem do jogador</p>
    <p><b>HAZARD</b> - responsável pela construção, posicionamento e imagem dos obstáculos</p>
    <p><b>SOUNDTRACK</b> - responsável pela trilha sonora no programa</p>
    <h1><b>BIBLIOTECAS UTILIZADAS</b></h1>
    <p><b>pygame</b> - amplamente utilizada para construção de jogos 2D em Python</p>
    <p><b>time</b> - fornece funções úteis relacionadas ao tempo</p>
    <p><b>random</b> - utilizada para gerar/selecionar números aleatórios</p>
    <p><b>os</b> - utilizada para interagir com o sistema operacional do dispositivo usado, neste programa, utilizamos métodos de acessos a arquivos no dispositivo (fontes e músicas)</p>
    <p><b>sys</b> - fornece acesso a funções que agem diretamente no interpretador Python, foi utilizada para avaliação de erros no acesso dos arquivos</p>
    <h1><b>Atributos da Classe GAME</b></h1>
    <p><b>screen:</b> Armazena a superfície da tela do jogo onde todos os elementos são desenhados.</p>
    <p><b>screen_size:</b> Contém as dimensões da tela do jogo.</p>
    <p><b>width e height:</b> Definem as dimensões fixas da tela do jogo (800x600 pixels).</p>
    <p><b>run:</b> Um booleano que controla a execução do loop principal do jogo.</p>
    <p><b>background:</b> Uma instância da classe Background, responsável pelo plano de fundo do jogo.</p>
    <p><b>player:</b> Uma instância da classe Player, que representa a nave controlada pelo jogador.</p>
    <p><b>hazard:</b> Uma lista que armazena os obstáculos (hazards) que o jogador deve evitar.</p>
    <p><b>render_text_bateuLateral e render_text_perdeu:</b> Armazenam textos para exibição ao jogador em caso de colisões ou game over.</p>
    <p><b>DIREITA e ESQUERDA:</b> Constantes que representam as teclas do teclado para movimentar a nave.</p>
    <p><b>mudar_x:</b> Um valor que representa a mudança na posição horizontal da nave com base nas teclas pressionadas.</p>
    <h1><b>Métodos da Classe GAME</b></h1>
    <p><b>__init__(self, size, fullscreen):</b> Inicializa o pygame, configura a tela do jogo, e define algumas configurações iniciais, como ocultar o mouse e definir o título da janela.</p>
    <p><b>elements_update(self, dt):</b> Atualiza os elementos do jogo. Por enquanto, chama o método update da classe Background, mas está preparado para ser expandido para outros elementos.</p>
    <p><b>elements_draw(self):</b> Desenha o plano de fundo na tela, chamando o método draw da classe Background.</p>
    <p><b>play_soundtrack(self) e play_sound(self, sound):</b> Métodos para tocar a trilha sonora e outros sons do jogo, verificando se os arquivos existem antes de tentar carregá-los.</p>
    <p><b>draw_explosion(self, screen, x, y):</b> Desenha uma imagem de explosão na tela em uma posição específica, usada quando o jogador colide com um hazard.</p>
    <p><b>handle_events(self):</b> Trata eventos do pygame, como pressionar teclas ou fechar a janela do jogo. Atualiza a variável mudar_x com base na entrada do usuário para mover a nave.</p>
    <p><b>write_message(self, message, R, G, B, x, y):</b> Exibe mensagens na tela em cores especificadas. É utilizada para mostrar mensagens como "GAME OVER".</p>
    <p><b>loop(self):</b> O loop principal do jogo, onde a lógica do jogo acontece. Atualiza a posição do fundo e dos hazards, verifica colisões, atualiza a pontuação e desenha os elementos na tela. Este é o coração do jogo e é responsável pela execução contínua até que o jogador perca ou vença.</p>
    <p><b>score_card(self, screen, h_passou, score):</b> Desenha o placar na tela, mostrando quantos obstáculos o jogador passou e a pontuação atual.</p>
</body>
</html>
