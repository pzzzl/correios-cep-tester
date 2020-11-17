# Correios CEP Tester

Um testador simples e prático da funcionalidade de <a href="https://buscacepinter.correios.com.br/app/endereco/index.php">busca de CEPs do Correios</a> construído com Python e Selenium.

```
python main.py
```

Correios CEP Tester é um Projeto Integrado da Universidade Municipal de São Caetano do Sul para os alunos do 4º Semestre de Análise e Desenvolvimento de Sistemas 2020.2.

<hr>

<h2>Escopo do teste</h2>

<ul>
  <li>Informar um valor correto - ou incorreto - para a busca de CEP do Correios</li>
  <li>Validar, de acordo com o resultado observado X o resultado esperado, se o teste foi atendido corretamente ou não</li>
  <li>Informar a quantidade de testes processados</li>
  <li>Informar a quantidade de testes bem sucedidos</li>
  <li>Informar a quantidade de testes falhos</li>
  <li>Informar a taxa de sucesso</li>
  <li>Gravar, em tempo de execução, todos os logs gerados em um arquivo .log</li>
</ul>

<hr>

<h3>Instalação</h3>

É importante ressaltar que o Python utiliza o Selenium como interface para o navegador web. Neste teste é utilizado o navegador Google Chrome, ainda que seja possível uma interface com o Mozilla Firefox. Outro ponto relevante é que dependemos da versão do Chrome para a execução. Para isso pode ser necessária uma verificação da versão do navegador digitando <span>chrome://version</span> na barra de endereços. Para fins de comparação de ambiente, a última versão foi executada para o Chrome v86.0.4240.198. Está incluso no repositório o chromedriver.exe compatível com esta versão.

Outro importante comando a ser executado na instalação (dentro da pasta do repositório) é:

```
pip install -r requirements.txt
```

Esse comando irá instalar todas as dependências necessárias para que o teste seja executado.

<hr>

<h3>Método de teste</h3>

O método de teste aplicado baseia-se na comparação de um resultado esperado X um resultado obtido, normalmente conhecido como "Teste do Resultado Esperado". É inerte à estrutura do teste um arquivo <span>testcases.json<span>, contendo um único set chave-valor (key-value) em que, para cada chave, o resultado esperado (valor) é comparado com o resultado obtido. Caso o resultado obtido <b>esteja integralmente contido</b> no resultado esperado, ocorre um match e a funcionalidade passa no teste. Caso contrário, a funcionalidade assume o estado de falha e reprova no teste.

É interessante ressaltar que os testcases funcionam como "garantias" de instrução. Ou seja: de nada ainda executar os testes se os casos de teste estiverem incorretos. Para isso, antes do desenvolvimento foram levantados 17 casos de teste para os quais eram conhecidos os resultados esperados. Assim é possível garantir que quaisquer divergências venham diretamente da ferramenta e não dos casos fornecidos para análise.

<hr>

<h3>Responsabilidades do teste</h3>

O teste é responsável por fornecer estatísticas e registros que possam identificar, com precisão, a eficiência da ferramenta ou mesmo do teste em si para fins de debug. Referente às estatísticas podemos definir, para cada caso de teste, os critérios a serem registrados como:

<ul>
  <li>Caso de teste</li>
  <li>Resultado</li>
  <li>Resultado esperado</li>
  <li>Resultado do teste (sucesso/falha)</li>
</ul>

Já para os aspectos gerais do teste:

<ul>
  <li>Testes processados</li>
  <li>Testes bem sucedidos</li>
  <li>Testes falhos</li>
  <li>Taxa de sucesso</li>
<ul>

<hr>

<h4>Explicação de cada caso de teste (testcase)</h4>

<ol>
  <li><b>"01310-932": "Avenida Paulista"</b> - CEP válido, espera resultado válido</li>
  <li><b>"09521-160": "Rua Santo Antônio"</b> - CEP válido, espera resultado válido</li>
  <li><b>"09521160": "Rua Santo Antônio"</b> - CEP válido porém mal-formatado, espera resultado válido</li>
  <li><b>"09530-060": "Rua Conceição"</b> - CEP válido, espera resultado válido</li>
  <li><b>"09510-102": "Rua Manoel Coelho"</b> - CEP válido, espera resultado válido</li>
  <li><b>"04288-080": "Rua Cônego José Norberto"</b> - CEP válido, espera resultado válido</li>
  <li><b>"09790-400": "Avenida Doutor José Fornari"</b> - CEP válido, espera resultado válido</li>
  <li><b>"04262-000": "Avenida Nazaré"</b> - CEP válido, espera resultado válido</li>
  <li><b>"00000-000": "Não há dados a serem exibidos"</b> - CEP inválido, espera resultado inválido</li>
  <li><b>"$$$": "Não há dados a serem exibidos"</b> - CEP não-numérico, espera resultado inválido</li>
  <li><b>"09090-650": "Rua Gonzaga Franco"</b> - CEP válido, espera resultado válido</li>
  <li><b>"50050-400": "Rua do Riachuelo"</b> - CEP válido, espera resultado válido</li>
  <li><b>"68552-218": "Rua Floresta"</b> - CEP válido, espera resultado válido</li>
  <li><b>"87065-320": "Rua Tulipa"</b> - CEP válido, espera resultado válido</li>
  <li><b>"12345-678": "Não há dados a serem exibidos"</b> - CEP inválido, espera resultado inválido</li>
  <li><b>"1": "Não há dados a serem exibidos"</b> - CEP inválido e caractere único, espera resultado inválido</li>
  <li><b>" ": "Não há dados a serem exibidos"</b> - CEP não informado, espera resultado inválido</li>
</ol>
  
Esse método "chave-valor" é extremamente eficiente quando há um conhecimento prévio sobre os casos a serem testados. Ter em mãos as respostas é o primeiro passo para poder avaliar novos casos. Ainda, é importante ressaltar o motivo pelo qual a pesquisa é feita em função do CEP e não do endereço: o CEP é um valor único. Funciona exatamente como um identificador do gênero do CPF ou RG. Sendo assim, utilizar o endereço como chave não é uma boa ideia, pois temos no mínimo 50 Avenidas Paulista pelo Brasil. Ou seja: um endereço pode retornar mais de um CEP enquanto um CEP não pode retornar mais de um endereço.

Exceção: existem alguns CEPs regionais que são desconsiderados para fins de endereços unicamente em vias.

<hr>

<h5>Créditos</h5>

<ul>
  <li>Andrei Amorim de Santana</li>
  <li>Bruno Peselli Piazzi</li>
  <li>Luan Cuba</li>
  <li>Luciano Feliciano Junior</li>
  <li>Michaelly Fernanda</li>
  <li>Steffany Candalaft Duram</li>
</ul>
