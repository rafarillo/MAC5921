## YOLO

* Atualmente:
    * Sistemas atuais de deteção de objetos resignificam classificadores para realizar detecção
* YOLO -> detecção de objeto como um problema de regressão
* De pixel para coordenadas de bounding box e probabilidades de classe.
* YOLO = you only look once
* Rede convolucial unica
* Prediz multiplos boundix boxes e classes de probabilidade para essas boxes
* YOLO é rápido
* YOLO enxerga a imagem toda durante treinamento (+ contexto)
* Dibide a imagem em um grid S x S. Se o centro cai na celula do grid, essa grid é responsável por detectar o objeto
* Total de 24 layer de convolução e 2 layers fully connected
* Realização de pré treinamento nas 20 layers
    * Adição de tanto de layer convolucional quanto layer fully connected no modelo pré treinado aumenta performance
* Layer final preduz ckasse de oribabukudade e coordenada da bounding box
* Utilização de função de ativação linear (no layer final)
    * Nos outros layers utiliza-se leaky rectified linear (ReLu)
    * $f(x) = \begin{cases} kx & x < 0 \\ x & x \ge 0 \end{cases}$
* Otimização feita usando MSE


## Dúvidas
Equação na seção 2 sobre confiança não entendi a equação