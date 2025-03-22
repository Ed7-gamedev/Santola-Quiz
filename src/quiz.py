import random

def criar_quiz():
    quiz = []
    temas = []
    
    perguntas = quiz_questions = [
    # Perguntas iniciais
    ("Qual é a capital de São Tomé e Príncipe?", "Geografia", "São Tomé", "Príncipe", "Neves", "Guadalupe"),
    ("Qual é o prato típico de São Tomé e Príncipe feito de banana-pão e peixe?", "Culinária", "Calulu", "Feijoada", "Moqueca", "Bacalhau à Brás"),
    ("Qual idioma é falado em São Tomé e Príncipe?", "Língua", "Português", "Inglês", "Francês", "Espanhol"),
    ("Quem foi o primeiro Presidente de São Tomé e Príncipe?", "Política", "Manuel Pinto da Costa", "Miguel Trovoada", "Evaristo Carvalho", "Patrice Trovoada"),
    ("Quem foi o cantor de São Tomé e Príncipe conhecido como 'O Grande General'?", "Música", "Jõao Seria", "Mister Page", "Pekeleu", "Pêpê Lima"),
    ("Qual é a principal atividade econômica de São Tomé e Príncipe?", "Economia", "Agricultura", "Turismo", "Pescas", "Mineração"),
    ("Qual destas comida é doce?", "Culinária", "Izaquente de Açucar", "Molho de Fogo", "Kissaka", "Calú"),
    ("Qual é o feriado nacional comemorado no dia 12 de julho?", "Cultura", "Dia da Independência", "Dia do Trabalhador", "Dia de São Tomé", "Dia da República"),
    ("Qual é o nome do criolo falado em São Tomé?", "Língua", "Forro", "Caboverdiano", "Lung'iyé", "Angolar"),
    ("Quem é a figura pública conhecida como 'Papá da Nação'?", "História", "Patríce Trovoada", "Miguel Trovoada", "Evaristo Carvalho", "Manuel Pinto da Costa"),
    ("Como se chama alguém que nasce na ilha do Príncipe?", "Cultura", "Santomense", "Moncó", "Principiano", "Principense"),
    ("Qual é a área protegida conhecida pela sua biodiversidade?", "Natureza", "Parque Nacional de Ôbo", "Reserva Natural de Monte Café", "Parque Natural do Príncipe", "Reserva de Santana"),
    ("Qual destas é nome de uma dança tradicional de São Tomé e Príncipe?", "Cultura", "Puita", "Samba", "Kizomba", "Fado"),
    ("Quem é a atual primeira-dama de São Tomé e Príncipe?", "Política", "Maria de Fátima Afonso Vila Nova", "Maria das Neves Vila Nova", "Célia Vila Nova", "Maria do Carmo"),
    ("Qual é o nome do parque natural marinho em São Tomé e Príncipe?", "Natureza", "Ilhéu das Rolas", "Ilha do Príncipe", "Ilhéu Santana", "Ilhéu Cabras"),
    ("Quem é o famoso poeta e escritor são-tomense?", "Literatura", "Alda do Espírito Santo", "Pepetela", "Mia Couto", "Luandino Vieira"),
    ("Qual é o nome do principal aeroporto de São Tomé e Príncipe?", "Geografia", "Aeroporto Internacional de São Tomé", "Aeroporto de Príncipe", "Aeroporto de Neves", "Aeroporto de Guadalupe"),
    ("Qual é o nome da principal universidade em São Tomé e Príncipe?", "Educação", "Universidade de São Tomé e Príncipe", "Universidade de Lisboa", "Universidade do Porto", "Universidade de Coimbra"),
    ("Qual é a moeda oficial de São Tomé e Príncipe?", "Economia", "Dobra", "Euro", "Dólar", "Franco CFA"),
    ("Qual é a principal religião praticada em São Tomé e Príncipe?", "Religião", "Cristianismo", "Islamismo", "Budismo", "Hinduísmo"),
    ("Qual é o esporte mais popular em São Tomé e Príncipe?", "Esportes", "Futebol", "Basquete", "Vôlei", "Handebol"),
    ("Qual é o nome da planta que é uma importante exportação de São Tomé e Príncipe?", "Economia", "Cacau", "Café", "Bambu", "Milho"),
    ("Qual é a ilha maior de São Tomé e Príncipe?", "Geografia", "São Tomé", "Príncipe", "Ilhéu das Rolas", "Ilhéu Santana"),
    ("Qual é o nome da ave endêmica de São Tomé e Príncipe conhecida por sua beleza?", "Natureza", "Pardal-de-são-tomé", "Papagaio-do-príncipe", "Cacatua-de-são-tomé", "Corvo-de-são-tomé"),
    ("Qual desta é a bebida alcoólica tradicional de São Tomé e Príncipe?", "Culinária", "Vinho Da Palma", "Cachaça", "Grogue", "Whisky"),
    ("Quem é o atual presidente de São Tomé e Príncipe?", "Política", "Carlos Vila Nova", "Manuel Pinto da Costa", "Evaristo Carvalho", "Miguel Trovoada"),
    ("Qual é o nome do estilo musical popular em São Tomé e Príncipe?", "Música", "Ússua", "Fado", "Samba", "Kizomba"),
    ("Qual é a principal unidade monetária de São Tomé e Príncipe?", "Economia", "Dobra", "Euro", "Dólar", "Franco CFA"),
    ("Qual é o nome do projeto ambiental que visa proteger a biodiversidade marinha em São Tomé e Príncipe?", "Natureza", "Projeto Tatô", "Projeto Ararinha", "Projeto Tamar", "Projeto Baleia Jubarte"),
    ("Qual é o nome do criador da bandeira de São Tomé e Príncipe?", "História", "Nuno Xavier", "Miguel Trovoada", "Manuel Pinto da Costa", "Evaristo Carvalho"),
    ("Qual é a data da independência de São Tomé e Príncipe?", "História", "12 de julho de 1975", "25 de abril de 1974", "7 de setembro de 1975", "1 de janeiro de 1975"),
    ("Qual é o nome da planta utilizada para fazer remédios tradicionais em São Tomé e Príncipe?", "Natureza", "Iboga", "Ginseng", "Aloe Vera", "Eucalipto"),
    ("Qual é o nome do arquipélago a que São Tomé e Príncipe pertencem?", "Geografia", "Golfo da Guiné", "Arquipélago dos Açores", "Arquipélago da Madeira", "Arquipélago de Cabo Verde"),
    ("Em que distrito fica Diogo Simão?", "Geografia", "Mezochi", "Caué", "Agua Grande", "Lembá"),
    ("Quem é a figura histórica conhecida como 'Pai da Independência' de São Tomé e Príncipe?", "História", "Amílcar Cabral", "Agostinho Neto", "Kwame Nkrumah", "Manuel Pinto da Costa"),
    ("Qual é a altitude do Pico Cão Grande?", "Geografia", "663 metros", "500 metros", "700 metros", "800 metros"),
    ("Qual a quantidade de ilhas que compõem São Tomé e Príncipe?", "Geografia", "14 ilhas", "10 ilhas", "5 ilhas", "3 ilhas"),
    ("Quem escreveu o livro 'Éramos Seis'?", "Literatura", "Alda do Espírito Santo", "Pepetela", "Conceição Lima", "Mia Couto"),
    ("Este trexo 'ozé nga bê m'ùn ê, milhó pa'un bê mô, pá kua na bila piolá', é da música?", "Música", "Núemia de Garrido", "Emae de Nino jalego", "Glato bèga de Africa Negra", "vivê de Gapa"),
    ("Qual é o nome da música tradicional tocada durante as festas de Santo António?", "Cultura", "Socopé", "Morna", "Kizomba", "Semba"),
    ("Qual é a ilha mais pequena de São Tomé e Príncipe?", "Geografia", "Ilhéu das Cabras", "Ilhéu de Santana", "Ilhéu das Rolas", "Ilhéu dos Marinheiros"),
    ("Qual é a taxa de alfabetização de São Tomé e Príncipe?", "Educação", "91.6%", "85.3%", "92.4%", "88.7%"),
    ("Qual é a principal atividade artística de São Tomé e Príncipe?", "Arte", "Música", "Escultura", "Dança", "Pintura"),
    ("Qual é a primeira universidade de São Tomé e Príncipe?", "Educação", "Universidade de São Tomé e Príncipe", "Universidade Lusíada", "Universidade IUCAI", "Universidade ISEC"),
    ("Qual é o nome do parque marinho reconhecido como patrimônio mundial da UNESCO?", "Natureza", "Parque Natural de Príncipe", "Parque Natural de Ôbo", "Parque Marinho de Santana", "Parque Marinho de Ilhéu"),
    ("Qual é a data da criação da moeda 'Dobra'?", "História", "1977", "1980", "1975", "1985"),
    ("Qual é o prato típico feito com matabala?", "Culinária", "Sôo", "Feijoada", "Moqueca", "Calú"),
    ("Qual é a principal ilha de cultivo de cacau?", "Economia", "Ilha de São Tomé", "Ilha do Príncipe", "Ilhéu das Rolas", "Ilhéu Santana"),
    ("Quem foi o primeiro ministro após a independência?", "Política", "Miguel Trovoada", "Evaristo Carvalho", "Manuel Pinto da Costa", "Patrice Trovoada"),
    ("Qual é a dança tradicional realizada durante festivais?", "Cultura", "Puita", "kizomba", "Fado", "Capoeira"),
    ("Qual é o nome da planta medicinal utilizada para tratar febres?", "Natureza", "Quina", "Iboga", "Eucalipto", "Aloe Vera"),
    ("A capital de São Tomé e Príncipe é conhecida por...", "Geografia", "São Tomé", "Príncipe", "Neves", "Guadalupe"),
    ("A principal atividade econômica do país é...", "Economia", "Agricultura", "Turismo", "Pescas", "Mineração"),
    ("O feriado nacional comemorado em 12 de julho é...", "Cultura", "Dia da Independência", "Dia do Trabalhador", "Dia de São Tomé", "Dia da República"),
    ("O criolo falado no país é chamado de...", "Língua", "Forro", "Caboverdiano", "Guineense", "Kriol"),
    ("A Constituição de São Tomé e Príncipe, inicialmente promulgada em 1975 foi revisada pela última vez em...", "Política", "2003", "1990", "1975", "2020"),
    ("A área protegida famosa pela biodiversidade é...", "Natureza", "Parque Nacional de Ôbo", "Reserva Natural de Monte Café", "Parque Natural do Príncipe", "Reserva de Santana"),
    ("A dança tradicional do país é...", "Cultura", "Puita", "Samba", "Kizomba", "Fado"),
    ("Em que dia descobriram a ilha do Príncipe...", "Cultura", "17 de Janeiro", "21 de Dezembro", "3 de Fevereiro", "20 de Janeiro"),
    ("O parque natural marinho do país é...", "Natureza", "Ilhéu das Rolas", "Ilha do Príncipe", "Ilhéu Santana", "Ilhéu Cabras"),
    ("Dos Seguintes quem é um  poeta e escritor Santomense...", "Literatura", "Alda do Espírito Santo", "Pepetela", "Mia Couto", "Luandino Vieira"),
    ("O principal aeroporto do país é...", "Geografia", "Aeroporto Internacional de São Tomé", "Aeroporto de Príncipe", "Aeroporto de Neves", "Aeroporto de Guadalupe"),
    ("A moeda oficial do país é...", "Economia", "Dobra", "Euro", "Dólar", "Franco CFA"),
    ("A ilha maior é chamada de...", "Geografia", "São Tomé", "Príncipe", "Ilhéu das Rolas", "Ilhéu Santana"),
    ("A famosa praia de São Tomé conhecida por suas tartarugas marinhas é...", "Praias", "Praia Jalé", "Praia das Sete Ondas", "Praia Melão", "Praia Piscina"),
    ("O cantor de sucesso internacional vindo de São Tomé é...", "Música", "Kalu Mendes", "Yuri da Cunha", "Anselmo Ralph", "C4 Pedro"),
    ("A maior estação de rádio de Stp é...", "Rádio", "RNSTP", "TVS", "Rádio Júbilar", "Rádio Boca Boca"),
    ("O edifício histórico que abriga o museu nacional é...", "Edifícios", "Forte de São Sebastião", "Palácio Presidencial", "Catedral de São Tomé", "Casa das Artes"),
    ("A celebridade conhecida por atuar no Progama Nós Por Cá é...", "Celebridades", "Papá Flaskin", "Patrice Trovoada", "Mister Page", "Sr Blechi"),
    ("A praia conhecida por suas águas cristalinas e atividades de mergulho é...", "Praias", "Praia Inhame", "Praia Jalé", "Praia Melão", "Praia Sete Ondas"),
    ("A instituição educativa mais antiga do país é...", "Instituições", "Liceu Nacional", "Universidade de São Tomé e Príncipe", "Patrice Lumumba", "Escola 12 de Julho"),
    ("A praia famosa por suas formações rochosas é chamada de...", "Praias", "Praia Piscina", "Praia Jalé", "Praia Sete Ondas", "Praia Inhame"),
    ("A celebridade conhecida como a voz da música tradicional são-tomense é...", "Celebridades", "Leonel Aguiar", "Cesária Évora", "Conceição Lima", "Yuri da Cunha"),
    ("O edifício conhecido por sua arquitetura colonial é...", "Edifícios", "Palácio Presidencial", "Forte de São Sebastião", "Casa das Artes", "Museu Nacional"),
    ("Qual o Intruso desta Lista", "Aleatório", "Sr Blechi", "Melé", "Pololó", "Pixotinho"),
    ("Complete o Proverbio : Caçô de tema...", "Criolo Forro", "Cá molé cú olhá Cotadú ", "na sá bon caçô", "Cá molé cedu", "sá pa dá pô"),
    ("Complete a mùsica: dodô cú sá dodô ná tê vlegonha fá...","Música", "familia dodô só cá tê vlegonha", "sela sun decê dó cé, bi pia non",  "cúma cú ami só cá tê", "punda ê sá nocentxi"),
    ("Quem foi que a mãe deixou uma fruta gigante quando faleceu", "Contos", "Buté", "Leo Boca Copo", "Beto", "Alda Espirito Santo"),
    ("De quem é o filme de curta metragem : Mina Kia", "Cinema", "Katya Aragão", "Guilherme de Carvalho", "Calemas", "Nenhum desses"),
    ("Complete a Música: Um de Junho", "Música", "D'já mina Pikina", "Dia das Crianças", "Queremos Pão", "2 de Junho"),
    ("Complete a Música: Nom bi pia Calá mum..", "Música", "Mô Plato suzu cú a ca cúme zête Cúlo Pê", "Punda un na sa Glavi fa", "Mô Caçô", "Fê favolô"),
    ("Complete a Música: Gândú ê ..,", "Música", "BÔ Alé Do mali, ni boca pixi...", "Pâ tudu pixi lêlê bÔ", "Qua Muntú  ô", "Cú a na Labefa"),
    ("O que significa : Sã Men Deçú", "Criolo Forro", "Madre-de-Deus", "Boa Noite", "Vai ao inferno", "é um prato típico"),
    ("O que significa : Glavi", "Crilo Forro", "Bonito", "Gravida", "Fome", "Branco"),
    ("Completa a música: Un tava cá bé chicolá di mun buassó...", "Música", "Um colê bá da mina nguê bega...", "antê un conçê bô", "Un dá uan topi", "holá un chiga na lá"),
    ("Esse trexo : Quem diria que eu estaria no altar de fato e gravata a esperar por ti, é de que música ", "Música", "Ô Mengai", "Milongo", "Tendê Kontagi", "Onde Anda"),
    ("Completa a música do GMC: Tás arrumada em santinha...", "Música que só quem é Santomense Lembra", "Tua familia é que não vê...", "Sou teu panco", "Quando tás cá na via", "De Joelho Pede desculpa"),
    ("Completa a música: Não sou Culpado", "Música que só os Santolas Lembram", "Tua dama me curte bué", "se ainda me amas", "e o problema não é meu", "Mulher não é problema"),
    ("Qual desses estilos musicais é tradicional de São Tomé?", "Música",  "Djambi", "Funana", "Zouk","Deixa",),
    ("Qual o nome do grupo musical de São Tomé e Príncipe famoso por suas canções folclóricas?", "Música", "Africa Negra", "Os Leais", "Quinteto Harmonia", "São Tomé Sound"),
    ("Qual artista santomense é conhecido pela música 'Mino Bô Bé Quacueda'?", "Música", "Juka", "Calú de Jau", "Pedrito", "Zé Delgado"),
    ("Qual desses instrumentos é comumente usado na música santomense?", "Música", "Dança Congo", "Bandolim", "Piano", "Baixo Elétrico"),
    ("Qual é um dos temas mais comuns nas músicas tradicionais santomenses?", "Música", "Histórias do cotidiano e resistência cultural", "Amor e romance", "Festas e celebrações", "Natureza e meio ambiente"),
    ("Qual desses artistas fez sucesso com a banda África Negra?", "Música", "João Seria", "Zeca Camargo", "Mário Mendes", "Carlos Pinta"),
    ("A música Demanda Pertence a qual Cantor?", "Música", "Alex Dinho", "Kalu Mendes", "Calemas", "Cafuca"),
    ("Qual desses artistas é a voz por trás da Música 'Ngandu ê'?", "Música", "Kalú Mendes", "Juka", "João Seria", "Zé Delgado"),
    ("Qual desses estilos musicais influenciou a música de São Tomé e Príncipe?", "Música", "Semba", "Fado", "Tango", "Reggae"),
    ("A Música 'Nom Molê', pertence...", "Música", "Aos Vibrados", " A Sangazuza", " A Africa Negra", " A Juka"),
    ("Em Que dia Descobriram a ilha de São Tomé", "História", "21 de Dezembro de 1470", "21 de Dezembro de 1471", "17 De Janeiro de 1470", "17 de Janeiro de 1471"),
    ("Quem fez o Remix 'Branca vai tá a Gritar Kidaleo' ? ", "Música", "DJ Puto Maravilha", "Dj Anjo Delax", "Dj Djeik Silva", "Nenhum Desses"),
    ("Qual Foi a Primeira Música do Mc Pipokinha?", "Música", "Toda Parada é Minha", "Catxinga", "Tô ir embora de mim", "Tá Mentir Para Mim"),
    ("Em que língua são predominantemente cantadas as músicas santomenses?", "Música", "Forro", "Português", "Inglês", "Francês"),
    ("Que feriado se Comemora no dia 6 de Setembro em STP?", "Cultura", "Dia das Forças Armadas", "Dia do Juramento a Bandeira", "Dia das Nacionalização das roças", "Dia das Tropas"),
    ("Esse trexo : 'Loço subi, Fúba subi, Sucri subi, tudo kúa subi', pertence a que música?", "Música", "Nom Molê", "Bô Buia", "Solê", "Kúa tá rijo"),
    ("O que significa 'Socope' na música santomense?", "Música", "Só com um pé", "Socos e Pontapés", "Mão non chão", "Com dois pés"),
    (" Como os navegadores portugueses baptizaram a ilha quedescobriram em 1471, no momento da descoberta", "História", "Ilha de Santo António", "Pagué", "Ilha do Príncipe", "Ilha de São Tomé"),
    (" A tragédia do marquês de Mântua e do imperador Carloto Magno foi escrita por?", "Cultura", "Baltazar Dias", "Caetano Costa Alegre", "Príncipe Don Carlos", "Marques de Mantua"),
    ("Em que ano ocorreu o massacre de batepá?", "Historia", "1953", "1970", "1950", " 3 de Fevereiro"),
    ("Onde se situa o Monumento em homenagem aos mártires do massacre de 3 de Fevereiro de 1953,?", "Cultura", "Fernão dias", "Praça da Independência", "Trindade", "Batepá"),
    ("O que é a Dança Congo?", "Música", "Uma dança tradicional santomense", "Um estilo de música eletrônica", "Um festival anual", "Um tipo de poesia cantada"),
    ("Em que ano foi errigido o Monumento em homenagem aos mártires do massacre de 3 de Fevereiro de 1953?", "Cultura", "2015", "1953", "2017", "2020"),
    ("Em STP, que feriado se Comemora no dia 3 de Fevereiro?", "Cultura_Geral", "Dia dos Martires", "Dia do Massacre de Batepá", "Dia do Rei Amador", "Dia das Crianças"),
    ("Qual é a cor padrão dos uniformes escolares dos alunos do 1º ao 6º ano em STP?", "Cultura_Geral", "Azul", "Cor de Creme", "Vermelho", "Branco"),
    ("Qual é a cor padrão dos uniformes escolares dos alunos do 7º ao 12º ano em STP?", "Cultura_Geral", "Cor de Creme", "Azul", "Vermelho", "Branco"),
    ("Killa_Z, Manu Fofucho e Trigre-T, faziam parte de que Grupo Músical?", "Música", "Os Vibrados", "Os GMC", "Sangazuza", "Kuá Nom"),
    ("Qual música venceu o Premio de Melhor Música do ano 2020 em STP?", "Música", "Boquitó de Vava Neviense", "Arca de Nóe de Alcino das Estrelas", "Fifofifó do Bulawê Pastelim", "Bomú Kelé dos Calemas"),
    ("Qual música venceu o Premio de Melhor Música do ano 2021 em STP?", "Música", "Arca de Nóe de Alcino das Estrelas", "Boquitó de Vava Neviense", "Fifofifó do Bulawê Pastelim", "Bomú Kelé dos Calemas"),
    ("Qual música venceu o Premio de Melhor Música do ano 2019 em STP?", "Música","Justiça de Edgar Seabra", "Boquitó de Vava Neviense", "Arca de Nóe de Alcino das Estrelas", "Fifofifó do Bulawê Pastelim"),
    ("Complete a Música, Palavra sá fogo...", "Música", "Amolê sá Justiça", "Lungua sá Zagué", "Cú ca pô Quemá", "anton, tomá cuidado cú bocá"),
    ("Complete a música. 'Quem quer conhencer boa gente'...", "Música", "Vem para saint city", "vem à São Tomé e Príncipe", "Quem Topa vida boa", "Vem à ilha do Príncipe"),
    ("Quem é o autoa da música 'Saint City'?", "Música", "Tunecas Prazeres", "Kalú Mendes", "Calemas", "Morena Santiago"),
    ("Quem é um dos principais representantes da nova geração de músicos santomenses?", "Música", "Calema", "Juka", "Africa Negra", "Zé Delgado"),
    ("Que Equipa foi a Grande Campeã de Futbol em STP no ano de 2020?", "Desporto", "6 de Setembro", "Operários do Príncipe", "Andorinhas", "Sporting de São Tomé"),
    ("Que Equipa venceu a SuperTaça se STP na epoca 2021/2022?", "Desporto", "Porto Real do Príncipe", "Operários do Príncipe", "6 de Setembro", "Sporting de São Tomé"),
    ("Que Equipa foi a Grande Campeã de Futbol em STP no ano de 2022?", "Desporto", "Agro-Sport de Monte Café", "Operários do Príncipe", "6 de Setembro", "Sporting de São Tomé"),
    ("Em que ano faleceu Alda do Espirito Santo?", "Literatura", "2010", "2009", "2011", "2012"),
    ("O poema Ilha Nua é de Autoria de...", "Literátura", "Alda do Espirito Santo", "Francisco José Tenreiro", "Olinda Beja", "Caetano Costa Alegre"),
    ("Complete o Poema: 'Ilha nua, coqueiros e palmares da terra natal...'?", "Literátura", "Mar azul das ilhas perdidas na conjuntura dos séculos", " A Caminho da roça", "Gritando a sede imensa do salgado mar", "Vegetação densa no horizonte imenso dos nossos sonhos."),
    ("Quantos são os Orgão de Soberania de STP?", "Política", "4", "2", "3", "5"),
    ("Qual é a forma de governo de São Tomé e Príncipe?", "Política", "República semipresidencialista", "Monarquia", "República parlamentarista", "Ditadura"),
    ("Quem é o chefe de governo segundo a Constituição de 2003?", "Política", "Primeiro-ministro", "Presidente", "Rei", "Ministro da Defesa"),
    ("Qual é a duração do mandato do Presidente da República?", "Política", "5 anos", "4 anos", "6 anos", "7 anos"),
    ("Quantos deputados compõem a Assembleia Nacional de São Tomé e Príncipe?", "Política", "55", "45", "60", "50"),
    ("Qual órgão tem o poder de legislar no país?", "Política", "Assembleia Nacional", "Presidência da República", "Tribunal Constitucional", "Governo"),
    ("Quem tem a responsabilidade de nomear o Primeiro-Ministro?", "Política", "Presidente da República", "Assembleia Nacional", "Povo", "Tribunal Constitucional"),
    ("Quantos artigos tem a Constituição de 2003?", "Política", "155", "120", "190", "200"),
    ("Qual é a idade mínima para um cidadão se candidatar à Presidência da República?", "Política", "35 anos", "30 anos", "40 anos", "25 anos"),

    # HISTÓRIA E CULTURA
    ("Em que ano São Tomé e Príncipe conquistou sua independência?", "História", "1975", "1960", "1980", "1995"),
    ("O que foi a Revolta de Batepá?", "História", "Uma revolta contra o trabalho forçado", "Uma guerra contra Portugal", "Uma crise econômica", "Uma guerra civil"),
    ("O que significa 'CST'?", "Cultura_Geral", "Compainha Santomense de Telecomunicações", "Centro de Sistema Tecnologicos ", "Sempre Juntos", "Empresa de Água e energia"),
    
    # GEOGRAFIA E NATUREZA
    ("Qual o nome do actual primeiro Ministro de STP?", "Política", "Americo Ramos", "Patríce Trovoada", "Carlos Vila Nova", "Celmira Sacramento"),
    ("Qual é a montanha mais alta do país?", "Geografia", "Pico de São Tomé", "Pico Cão Grande", "Monte Carmo", "Serra Malanza"),
    ("Quantas são as estações do país?", "Geografia", "2", "3", "4", "5"),
    ("O que é o Pico Cão Grande?", "Geografia", "Uma formação vulcânica", "O maior rio do país", "Uma reserva florestal", "Uma ilha"),
    ("Qual o nome do actual presidente da Assembleia Nacional de STP?", "Política","Celmira Sacramento", "Patríce Trovoada", "Americo Ramos", "Delfim Neves"),
    
    # MÚSICA E ARTISTAS SANTOMENSES
    ("Em que ano foi aberto a actual Escola Patríce Lumumba?", "Cultura_Geral", "21 de Setembro de 1952", "21 de Setembro de 1954", "22 de Agosto de 1952", "22 de Agosto de 1954"),
    ("O mês da Cultura na ilha do Príncipe é celebrado em...", "Cultura", "Agosto", "Abril", "Maio", "Fevereiro"),
    ("O que caracteriza a música Puita?", "Música", "Uso de tambores e canto responsorial", "Batida eletrônica", "Forte influência do fado", "Uso de saxofone"),
    ("Complete un,bô,ê,non,nansê... ?", "Crioulo Forro", "ínê", "ami", "êlê", "mu"),


    # GASTRONOMIA
    ("Qual é um prato típico santomense?", "Gastronomia", "Calulu", "Feijoada", "Cachupa", "Moqueca"),
    ("Qual destes peixes é amplamente utilizado na culinária de São Tomé e Príncipe?", "Gastronomia", "Peixe-Andala", "Bacalhau", "Atum", "Salmão"),
    ("Qual é um doce tradicional santomense?", "Gastronomia", "açucarinha", "Pastel de nata", "Doce de leite", "Pudim de leite"),
    
    ("Qual destas expressões em crioulo forro não exprime o sentimente de aprovação?", "Crioulo Forro", "tón ganá Bô", "Ká Potô", "Bô subli", "ya ku sê lê ë"),

    ("Quem é o atual Presidente da República de São Tomé e Príncipe?", "Política", "Carlos Vila Nova", "Evaristo Carvalho", "Manuel Pinto da Costa", "Patrice Trovoada"),
    ("Quantos distritos administrativos existem em São Tomé e Príncipe?", "Política", "7", "5", "9", "10"),
    ("Qual foi o primeiro partido político do país?", "Política", "MLSTP/PSD", "ADI", "PCD", "MDFM"),
    ("O que é a Autonomia da Ilha do Príncipe?", "Política", "Um estatuto especial concedido à ilha", "Uma região independente", "Um partido político", "Um movimento separatista"),
    ("Em que dia ocorreu a trágica tentativa de golpe de Estado no Quartel das Forças Armadas de STP?", "Política", "22 de Novembro de 2022", "22 de Novembro de 2023", "27 de Novembro de 2022", "27 de Novembro de 2023"),
    ("Onde nasceu o Músico Fradique Mendes dos Calemas?", "Música", "Roça Ribeira Peixe", "Roça de Angolares", "Ilha do Píncipe", "Portugal"),
    ("Dos irmãos Calemas, Qual o mais velho?", "Música", "O Fradique ", "O António", "Os dois têm a mesma idade, são gêmeos", "Não Sei"),
    ("OQual a música Santomense mais escutada no mundo?", "Música", "Nossa Vez dos Calemas", "Imigração de Leu Boca Copo", "Onde Anda dos Calemas", "O remix Branca vai tá a gritar Kidaleo"),
    ("Com mais de meio milhão de visualização, qual destas músicas tem mais visualização em relação as outras?", "Música", "Imigração de Leu boca copo", "Vai se dar mal de Babilonia", "Adeus dos Ra´zes da PTF", "Maria dos Raízes da PTF"),
    ("Qual das seguintes músicas não ultrapassou o marco de 1 milhão de visualizações no Youtube?", "Música", " Na Solafá de Tubias Vaiana", "Mino bô bê kua Cueda de Jõa Seria", "nha terra ê chora de Camilo Domingos", "Angelina de Juka"),
    
    
    ("O que significa o ditado santomense 'Péxi ê ku bo boca maji, mé bo ka podi kulá bo dente'?", "Provérbios", "Cuidado com o que diz, pois pode se voltar contra você", "Se quer peixe, deve pescar", "Nunca confie em estranhos", "A boca fala o que o coração sente"),

    ("Qual é o significado do provérbio 'Kuá ki fuá bô ka tá xêlu'?", 
     "Provérbios", 
     "Cada um colhe o que planta", 
     "O mar sempre devolve o que leva", "Quem tudo quer, nada tem", "O tempo cura todas as feridas"),

    ("O que significa a expressão santomense 'Lêvê-lêvê'?", 
     "Crioulo", 
     "Devagar", 
     "Rápido", "Com força", "Para trás"),

    ("O que quer dizer o ditado 'Bô ka kulê, bô ka podi tê fãdá'?", 
     "Provérbios", 
     "Sem esforço, não há recompensa", 
     "Quem muito fala, pouco faz", "A paciência é uma virtude", "Quem corre cansa, quem anda alcança"),

    ("O que significa 'Bô sá fuá, bô sá xêlu'?", 
     "Provérbios", 
     "Quem planta, colhe", 
     "Quem espera, sempre alcança", "A vida é um jogo", "Nunca deixe para amanhã o que pode fazer hoje"),

    ("Como se diz 'Bom dia' em forro?", 
     "Crioulo", 
     "Dôbla", 
     "Ôxi", "Alô", "Lusá"),

    ("O que significa 'Zunta-mama' em crioulo santomense?", 
     "Crioulo", 
     "Reunião de família ou conversa séria", 
     "Brincadeira", "Festa", "Dança típica"),

    ("O que quer dizer o ditado 'Bô ka fé, bô ka podi gánhá'?", 
     "Provérbios", 
     "Sem trabalho, não há sucesso", 
     "O tempo é o melhor remédio", "A sorte protege os audazes", "Quem tem boca vai a Roma"),

    ("O que significa 'Tudu mondu ka podi sê kinzú'?", 
     "Provérbios", 
     "Nem todos podem ser líderes", 
     "O tempo voa", "Quem cala, consente", "A união faz a força"),

    ("O que significa a palavra 'Mionga' em crioulo santomense?", 
     "Crioulo", 
     "Casa", 
     "Comida", "Trabalho", "Dinheiro"),

    ("O que quer dizer 'Bô ká bê, bô ká txê'?", 
     "Provérbios", 
     "Se não ouvir, não vai aprender", 
     "A pressa é inimiga da perfeição", "Quem muito se abaixa, mostra o traseiro", "Água mole em pedra dura, tanto bate até que fura"),

    ("O que significa 'Fidju di mon' em crioulo santomense?", 
     "Crioulo", 
     "Órfão", 
     "Filho mais velho", "Neto", "Primo"),

    ("O que quer dizer 'Bô ka ta suá na ôbô di outo'?", 
     "Provérbios", 
     "Cada um deve resolver seus próprios problemas", 
     "O silêncio vale ouro", "A mentira tem perna curta", "A justiça tarda, mas não falha"),

    ("Qual é o significado de 'Mininu ku sá minda ka podi papia'?", 
     "Provérbios", 
     "Criança que não respeita, não pode falar", 
     "Quem dorme, perde", "O mundo dá voltas", "Cada um com seus problemas"),

    ("O que significa a expressão 'Xê mundu'?", 
     "Crioulo", 
     "Olha isso!", 
     "Bom dia!", "Vamos embora!", "Que estranho!"),

    ("O que quer dizer o provérbio 'Bicho ku ka ten kabéça, olê ba kó'?", 
     "Provérbios", 
     "Quem não tem juízo, se perde", 
     "A vida é curta", "O mar sempre devolve o que leva", "A sorte não bate duas vezes"),

    ("O que significa a palavra 'Fidju di Tera'?", 
     "Crioulo", 
     "Filho da terra", 
     "Turista", "Amigo", "Forasteiro"),

    ("O que quer dizer o ditado 'Bô ká flá fá, bô ka podi kumpá su'?", 
     "Provérbios", 
     "Não fale do que você não sabe", 
     "Se quer ser respeitado, respeite", "A verdade sempre vence", "Quem muito quer, nada tem"),

    ("O que significa a expressão 'Bô ka bôbô, bô ka podi kotó'?", 
     "Provérbios", 
     "Sem esforço, não há vitória", 
     "O tempo cura tudo", "A união faz a força", "Quem semeia vento, colhe tempestade"),

    ("O que quer dizer 'Sá fla sá gosi, sá flá sá manglo'?", 
     "Provérbios", 
     "Fale no momento certo", 
     "Quem espera sempre alcança", "O silêncio vale ouro", "Tudo tem seu tempo"),
    
    
    ("Quem é considerado um dos maiores poetas de São Tomé e Príncipe, autor de 'O Útero da Casa'?", "Literatura", "Conceição Lima", "Francisco Costa Alegre", "Alda Espírito Santo", "Albertino Bragança"),
    ("Qual poeta santomense publicou 'A Dolorosa Raiz do Micondó'?", "Literatura", "Conceição Lima", "Alda Espírito Santo", "Maria Manuela Margarido", "Albertino Bragança"),
    ("Qual escritora santomense é autora do livro 'O Jogo de Izidro'?", "Literatura", "Olinda Beja", "Conceição Lima", "Alda Espírito Santo", "Maria de Jesus Trovoada"),
    ("Quem foi a primeira mulher a publicar um livro de poesia em São Tomé e Príncipe?", "Literatura", "Alda Espírito Santo", "Maria Manuela Margarido", "Conceição Lima", "Olinda Beja"),
    ("Qual escritor santomense escreveu 'O Monhé das Cobras'?", "Literatura", "Albertino Bragança", "Francisco Costa Alegre", "Olinda Beja", "Conceição Lima"),
    ("Qual autora santomense escreveu o livro 'Pingos de Chuva'?", "Literatura", "Olinda Beja", "Alda Espírito Santo", "Maria Manuela Margarido", "Albertino Bragança"),
    ("Quem escreveu 'Éramos Felizes e Não Sabíamos'?", "Literatura", "Olinda Beja", "Conceição Lima", "Alda Espírito Santo", "Albertino Bragança"),
    ("Qual poeta santomense foi um dos primeiros a abordar a questão da identidade nacional na literatura?", "Literatura", "Francisco Costa Alegre", "Alda Espírito Santo", "Conceição Lima", "Albertino Bragança"),
    ("Quem é o autor do poema 'Testamento'?", "Literatura", "Francisco Costa Alegre", "Alda Espírito Santo", "Olinda Beja", "Albertino Bragança"),
    ("Qual poeta santomense escreveu 'Levantados do Chão'?", "Literatura", "Francisco Costa Alegre", "Alda Espírito Santo", "Conceição Lima", "Maria Manuela Margarido"),
    ("Quem foi a escritora santomense homenageada no Festival Literatura-Mundo em 2021?", "Literatura", "Olinda Beja", "Conceição Lima", "Alda Espírito Santo", "Albertino Bragança"),
    ("Qual dessas escritoras santomenses também é professora e contadora de histórias?", "Literatura", "Olinda Beja", "Alda Espírito Santo", "Conceição Lima", "Maria Manuela Margarido"),
    ("Qual poeta santomense é autora de 'O Útero da Casa'?", "Literatura", "Conceição Lima", "Olinda Beja", "Alda Espírito Santo", "Maria Manuela Margarido"),
    ("Qual dessas escritoras foi uma das vozes mais ativas no movimento de independência de São Tomé e Príncipe?", "Literatura", "Alda Espírito Santo", "Francisco Costa Alegre", "Conceição Lima", "Albertino Bragança"),
    ("Qual autor santomense escreveu sobre a colonização e resistência africana em suas obras?", "Literatura", "Francisco Costa Alegre", "Albertino Bragança", "Alda Espírito Santo", "Maria Manuela Margarido"),
    ("Quem escreveu 'À Sombra do Oká'?", "Literatura", "Olinda Beja", "Conceição Lima", "Alda Espírito Santo", "Francisco Costa Alegre"),
    ("Qual dessas escritoras também é conhecida por sua atuação política e cultural?", "Literatura", "Alda Espírito Santo", "Olinda Beja", "Conceição Lima", "Albertino Bragança"),
    ("Qual é o nome do poeta santomense que usou sua poesia para expressar sua luta contra a opressão colonial?", "Literatura", "Francisco Costa Alegre", "Albertino Bragança", "Alda Espírito Santo", "Conceição Lima"),
    ("Quem foi o autor santomense que também atuou como diplomata e jornalista?", "Literatura", "Albertino Bragança", "Francisco Costa Alegre", "Olinda Beja", "Conceição Lima"),
    ("Qual dessas escritoras é conhecida por sua poesia de forte teor social e político?", "Literatura", "Alda Espírito Santo", "Conceição Lima", "Olinda Beja", "Maria Manuela Margarido"),
    ("Qual poeta santomense escreveu o livro 'No País do Tchiloli'?", "Literatura", "Olinda Beja", "Conceição Lima", "Alda Espírito Santo", "Albertino Bragança"),
    ("Quem é a autora do livro 'Histórias da Gravana'?", "Literatura", "Olinda Beja", "Conceição Lima", "Alda Espírito Santo", "Maria Manuela Margarido"),
    ("Qual escritor santomense escreveu sobre a diáspora africana em suas obras?", "Literatura", "Albertino Bragança", "Francisco Costa Alegre", "Olinda Beja", "Conceição Lima"),
    ("Qual poeta santomense é conhecida por retratar o cotidiano santomense em suas poesias?", "Literatura", "Conceição Lima", "Olinda Beja", "Alda Espírito Santo", "Maria Manuela Margarido"),
    ("Quem foi o primeiro escritor santomense a ter uma obra publicada?", "Literatura", "Francisco Costa Alegre", "Albertino Bragança", "Alda Espírito Santo", "Conceição Lima"),
    ("Qual escritor santomense utilizou a poesia como forma de resistência ao colonialismo?", "Literatura", "Francisco Costa Alegre", "Alda Espírito Santo", "Conceição Lima", "Olinda Beja"),
    ("Quem escreveu 'O Reino de Caliban'?", "Literatura", "Alda Espírito Santo", "Conceição Lima", "Francisco Costa Alegre", "Albertino Bragança"),
    ("Qual escritora santomense é conhecida por sua ligação com a cultura angolana e moçambicana?", "Literatura", "Olinda Beja", "Conceição Lima", "Alda Espírito Santo", "Maria Manuela Margarido"),
    ("Quem foi a primeira mulher santomense a publicar um livro de contos?", "Literatura", "Maria Manuela Margarido", "Olinda Beja", "Alda Espírito Santo", "Conceição Lima"),
    

    # CIDADES E DISTRITOS
    ("Qual é a capital de São Tomé e Príncipe?", "Geografia", "São Tomé", "Santo António", "Neves", "Trindade"),
    ("Qual é a cidade mais populosa do país?", "Geografia", "São Tomé", "Neves", "Santo António", "Guadalupe"),
    ("Qual cidade é a capital da Ilha do Príncipe?", "Geografia", "Santo António", "Ponta Mina", "Porto Alegre", "Monte Café"),
    ("Quantos distritos administrativos existem na Ilha de São Tomé?", "Geografia", "6", "5", "4", "3"),
    ("Qual distrito fica mais ao sul da Ilha de São Tomé?", "Geografia", "Caué", "Mé-Zóchi", "Lembá", "Água Grande"),
    ("Qual distrito abriga a capital São Tomé?", "Geografia", "Água Grande", "Cantagalo", "Mé-Zóchi", "Lembá"),
    ("Onde fica a cidade de Guadalupe?", "Geografia", "Distrito de Lobata", "Distrito de Lembá", "Distrito de Mé-Zóchi", "Distrito de Cantagalo"),
    ("Qual distrito abriga a Roça Monte Café?", "Geografia", "Mé-Zóchi", "Lobata", "Cantagalo", "Água Grande"),
    ("Qual é o distrito mais ao norte de São Tomé?", "Geografia", "Lobata", "Lembá", "Mé-Zóchi", "Cantagalo"),
    ("Onde fica a cidade de Neves?", "Geografia", "Lembá", "Lobata", "Água Grande", "Caué"),

    # EDIFÍCIOS E LOCAIS HISTÓRICOS
    ("Qual é o edifício que abriga a sede do governo de São Tomé e Príncipe?", "História", "Palácio do Povo", "Assembleia Nacional", "Palácio Presidencial", "Câmara Municipal"),
    ("O Palácio Presidencial de São Tomé e Príncipe está localizado em qual cidade?", "História", "São Tomé", "Guadalupe", "Santo António", "Neves"),
    ("Qual é a igreja mais antiga de São Tomé e Príncipe?", "História", "Sé Catedral de São Tomé", "Igreja de Santo António", "Igreja de Guadalupe", "Igreja de Neves"),
    ("Onde está localizada a Roça Agostinho Neto?", "História", "Perto de Guadalupe", "Em Trindade", "No sul da ilha", "Na Ilha do Príncipe"),
    ("O Forte de São Sebastião atualmente abriga o quê?", "História", "Museu Nacional", "Palácio Presidencial", "Base Militar", "Universidade"),
    ("Qual local histórico é conhecido por suas antigas plantações de café?", "História", "Roça Monte Café", "Roça Água Izé", "Roça São João", "Roça Diogo Vaz"),
    ("Onde está localizada a Roça Água Izé?", "História", "Cantagalo", "Mé-Zóchi", "Lembá", "Lobata"),
    ("O que se pode encontrar no Forte de São Jerônimo?", "História", "Ruínas de um forte colonial", "Um hotel de luxo", "A residência do presidente", "Uma estação de trem"),
    ("Qual é um dos principais marcos arquitetônicos da cidade de São Tomé?", "História", "Palácio do Povo", "Câmara Municipal", "Mercado Municipal", "Estádio Nacional 12 de Julho"),
    ("A Roça São João foi transformada em quê?", "História", "Centro cultural e hotel", "Sede do governo", "Escola agrícola", "Base militar"),

    # PRAIAS E ILHÉUS
    ("Qual é uma das praias mais famosas de São Tomé?", "Turismo", "Praia das Sete Ondas", "Praia dos Tamarindos", "Praia de Santa Rita", "Praia do Governador"),
    ("Onde fica a Praia Jalé?", "Turismo", "Extremo sul de São Tomé", "Perto de Neves", "Na Ilha do Príncipe", "No norte da ilha"),
    ("Qual destas ilhotas pertence a São Tomé e Príncipe?", "Turismo", "Ilhéu das Rolas", "Ilha do Sal", "Ilhéu de Luanda", "Ilhéu do Príncipe"),
    ("O que atrai turistas ao Ilhéu das Rolas?", "Turismo", "Linha do Equador", "Forte colonial", "Lagoas vulcânicas", "Cachoeiras"),
    ("Onde se localiza a Praia Inhame?", "Turismo", "No sul de São Tomé", "Na Ilha do Príncipe", "Em Neves", "Em Guadalupe"),
    ("O que faz a Praia dos Tamarindos ser especial?", "Turismo", "Águas cristalinas e areia branca", "Ondas fortes para surf", "Fica na Ilha do Príncipe", "É uma praia vulcânica"),
    ("Qual ilhéu fica próximo à capital São Tomé?", "Turismo", "Ilhéu das Cabras", "Ilhéu das Rolas", "Ilhéu Santana", "Ilhéu Bom Bom"),
    ("O Ilhéu Bom Bom faz parte de qual ilha?", "Turismo", "Príncipe", "São Tomé", "Ilhéu das Rolas", "Lobata"),

    # MONTANHAS E PONTOS NATURAIS
    ("Qual é o ponto mais alto de São Tomé e Príncipe?", "Geografia", "Pico de São Tomé", "Pico Cão Grande", "Monte Carmo", "Serra Malanza"),
    ("Onde se encontra o Pico Cão Grande?", "Geografia", "Caué", "Lembá", "Cantagalo", "Mé-Zóchi"),
    ("Qual destas formações é um marco natural impressionante do país?", "Geografia", "Pico Cão Grande", "Lagoa Azul", "Ilhéu das Rolas", "Praia Inhame"),
    ("Onde está localizado o Parque Natural Obô?", "Geografia", "Tanto em São Tomé quanto no Príncipe", "Apenas na Ilha do Príncipe", "Apenas em São Tomé", "Em Ilhéu das Rolas"),
    ("O Rio Iô Grande é conhecido por quê?", "Geografia", "Ser o maior rio de São Tomé", "Dividir as ilhas", "Ter origem vulcânica", "Ser navegável o ano todo"),
    ("Onde fica a Lagoa Azul?", "Geografia", "No norte de São Tomé", "Na Ilha do Príncipe", "No centro de São Tomé", "Perto do Pico de São Tomé"),

    # INFRAESTRUTURA E TRANSPORTE
    ("Qual é o principal aeroporto do país?", "Infraestrutura", "Aeroporto Internacional de São Tomé", "Aeroporto de Santo António", "Aeroporto de Guadalupe", "Aeroporto de Neves"),
    ("Qual é o principal porto do país?", "Infraestrutura", "Porto de Ana Chaves", "Porto de Santo António", "Porto das Rolas", "Porto de Lembá"),
    ("Onde se localiza o Estádio Nacional 12 de Julho?", "Infraestrutura", "São Tomé", "Guadalupe", "Neves", "Santo António"),
    ("Qual é a principal rodovia que liga o norte ao sul da Ilha de São Tomé?", "Infraestrutura", "EN1", "EN3", "EN2", "Rodovia do Príncipe"),
    ("O que conecta São Tomé à Ilha do Príncipe?", "Infraestrutura", "Avião e barco", "Ponte", "Trem", "Apenas barcos"),



]

    random.shuffle(perguntas)
    for i in range(len(perguntas)):
        pergunta, tema, resposta_correta, resposta_errada1, resposta_errada2, resposta_errada3 = perguntas[i]
        quiz.append([pergunta, tema, resposta_correta, resposta_errada1, resposta_errada2, resposta_errada3])
    
    return quiz

# Exemplo de uso
quiz = criar_quiz()



# Criar a matriz
matriz_quiz = criar_quiz()




