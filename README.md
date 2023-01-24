A DublAI é uma ferramenta de dublagem e traducao natural usando inteligencia artificial para recriar a voz original e sua entonacoes e nuances de forma a se tornar uma ferramenta com aplicacoes de amplo espectro tais como:

Governos internacionais - traduzindo conversas com a voz original e quebrando barreiras linguisticas. Rodando em tempo real com apenas um curto delay ela é capaz de acompanhar uma conversa de forma instantanea. Governos que falam diferentes linguas passariam a se comunicar de forma mais clara e tranquila.

Canais de TV e noticias - permite manter a originalidade da noticia mas ainda permitindo que qualquer pessoa possa entender sem a necessidade de legendas. DublAI, separa o audio das vozes, traduz e dubla na nova lingua com extrema naturalidade e depois as insere novamente ao video usando sincronizacao labial.

Estudios de dublagem - DublAI foi desenhada especialmente para esta tarefa, permite dublar um filme inteiro com centenas de personagens respeitando suas vozes e caracteristicas de fala com naturalidade. Filmes de até 5horas com até 90gb em formato mp4, mkv e avi. Em nossos testes ela operou quase sem assistencia, dublando completamente os filmes, sendo necessario pouco ou quase nenhum processo de pos edicao.

Educacao - permitindo ter uma maior imersao da lingua, funciona como um espelho, mostrando como falar corretamente.

Comunicacao integrada - usando uma api veloz é possivel integrar DublAI em comunicadores como telegran e whatsapp, que dublar audios em qualquer idioma listado em nossa documentacao. ( essa funcao nao trabalha ainda com videos)

Hoshi Sato se apresenta de 3 formas.
API - para integracao com comunicadores, radios, noticias, e etc. Trabalha apenas com audio. 
Web - dubla qualquer filme que forma independente e autonoma.
App - dubla qualquer conversa quase que instantaneamente, podendo ser usada em palestras, conversas ao vivo, reunioes e etc.

Ela trabalha usando um modelo treinando em 8 linguas com 1.1b de parametros, de vozes, nunces, e padroes de linguages. Tudo para proporcionar que Hoshi Sato possa dublar qualquer voz com perfeição em qualquer uma das 7 linguas opcionais. 
Ela trabalha dublando em qualquer direcao. De Ingles para portugues, ou de portugues para ingles. 

A ferramenta nao armazena dados dos arquivos dublados, novas versoes do modelo serao lancadas com melhorias e aperfeicoamentos. 

A ferramenta trabalha completamente de forma autonoma nao dependendo de nenhum operador do sistema, apenas um ambiente aws bem configurado.

## Instalação

Para utilizar, é necessário ter as seguintes dependências instaladas:
- Python 3.6 ou superior
- Tensorflow 2.0 ou superior
- Librosa 0.8.0 ou superior

Você pode instalar as dependências necessárias executando o seguinte comando:

`pip install -r requirements.txt`

## Uso

DublAI se apresenta de 3 formas:
- API: para integração com comunicadores, rádios, notícias, etc. Trabalha apenas com áudio.
- Web: dubla qualquer filme de forma independente e autônoma.
- App: dubla qualquer conversa quase que instantaneamente, podendo ser usada em palestras, conversas ao vivo, reuniões, etc.

Para utilizar DublAI, você precisa especificar o idioma de origem e o idioma de destino, além do arquivo de áudio ou vídeo que deseja dublar.

Exemplo de uso:

`python DublAI.py --src_lang pt --tgt_lang en --src_file my_video.mp4`

## Contribuindo

Contribuições são sempre bem-vindas! Por favor, leia nossas [diretrizes de contribuição](https://github.com/caioross/DublAI/blob/master/CONTRIBUTING.md) antes de começar a contribuir.

Até o momento, o projeto já possui as seguintes funcionalidades implementadas:
- Tokenização de áudios e vídeos
- Treinamento de modelo de IA com dados de filmes em português e inglês
- Dublagem de áudio com a voz original simulada em outro idioma
- Integração com aplicativos de comunicação (API)
- Interface Web para dublagem de filmes
- Interface App para dublagem de conversas em tempo real

Para rodar o projeto, siga os seguintes passos:
1. Clone o repositório: `git clone https://github.com/caioross/DublAI.git`
2. Entre na pasta do projeto: `cd DublAI`
3. Instale as dependências: `pip install -r requirements.txt`
4. Execute o script principal: `python DublAI.py --src_lang [idioma_origem] --tgt_lang [idioma_destino] --src_file [arquivo_de_audio_ou_video]`

Lembre-se de substituir os parâmetros entre colchetes pelos valores desejados.

## Licença

DublAI é distribuído sob a licença de teste Beta para uma comunidade Restrita de desenvolvedores.
