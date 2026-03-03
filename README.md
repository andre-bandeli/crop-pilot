# 🚜 CropPilot: Route Optimization for Digital Farming

> API de otimização logística que utiliza Algoritmos Genéticos para reduzir custos operacionais e emissão de carbono em frotas agrícolas.
---

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)  
[![Django](https://img.shields.io/badge/Django-4.2-brightgreen)](https://www.djangoproject.com/)  
--- 


## 📌 O Desafio do 'Caixeiro Viajante' no Campo

> "José é caixeiro-viajante: ele desloca-se da fábrica até as lojas dos clientes, para entregar a mercadoria e receber novas encomendas, e volta à fábrica ao final. E gostaria de saber qual é o itinerário mais curto que pode tomar passando por todas as lojas." [Fonte: IMPA](https://impa.br/notices/folha-o-problema-do-caixeiro-viajante/)

Planejar rotas eficientes para máquinas agrícolas (colheitadeiras, tratores) em grandes propriedades é um desafio complexo:  
- **Desperdício de recursos**: Rotas redundantes aumentam consumo de combustível.  
- **Tempo ocioso**: Operações manuais levam a altas horas diárias de improdutividade.  
- **Custo elevado**: Falta de otimização provoca alto custo a agricultura familiar e para o agronegócio brasileiro.  
- **Impacto**: O trajeto ineficiente aumenta o consumo de diesel e acelera a depreciação do maquinário.
- **Complexidade**: O problema escala exponencialmente conforme o número de talhões e restrições de carga aumentam ($NP-hard$).

---

## 🚀 Solução Técnica
O **CropPilot** resolve o problema através de **Computação Evolutiva**, utilizando a biblioteca DEAP para implementar um Algoritmo Genético (AG) customizado para o contexto do agronegócio. 

- **Codificação**: Indivíduos representados por sequências de coordenadas geográficas.
- **Fitness Function**: Minimização da distância euclidiana total (considerando a curvatura da Terra via cálculos geodésicos com Shapely).
- **Operadores Evolutivos**: Seleção por torneio, crossover de ordem (OX) para manter a integridade da rota e mutação por inversão.

---

## 💻 Stack Tecnológica  
| Componente               | Tecnologias                                                                 |  
|--------------------------|-----------------------------------------------------------------------------|  
| **Core**              | Python 3.10
**Framework**               | Django & Django REST Framework (DRF) 
| **Algoritmo**            | DEAP (Distributed Evolutionary Algorithms in Python)                        |  
| **Geoprocessamento**     | Geopandas, Shapely                                                         |
| **Infraestrutura**       | Docker (opcional), PostgreSQL (Para validação local)                                             |  

---

## 🗂️ Documentação da API  

### Endpoint: `POST /api/optimize/` 
Calcula a sequência ideal de visitação para um conjunto de pontos.
 
**Requisição:**  
```json  
{
    "machine_id": 1,
    "points": [
        {
            "name": "Sede da Fazenda",
            "latitude": -15.5400,
            "longitude": -55.1700,
            "is_depot": true,
            "estimated_load": 0
        },
        {
            "name": "Talhão 1",
            "latitude": -15.5402,
            "longitude": -55.1703,
            "is_depot": false,
            "estimated_load": 500
        },
                {
            "name": "Talhão 2",
            "latitude": -15.1402,
            "longitude": -55.1703,
            "is_depot": false,
            "estimated_load": 500
        },
                {
            "name": "Talhão 3",
            "latitude": -16.1402,
            "longitude": -55.1703,
            "is_depot": false,
            "estimated_load": 500
        },
                {
            "name": "Talhão 4",
            "latitude": -16.1402,
            "longitude": -55.1723,
            "is_depot": false,
            "estimated_load": 500
        }
    ]
}
```

**Resposta (Sucesso 200):**
```json
{
    "optimized_route": [
        [
            "Sede da Fazenda",
            "Talhão 2",
            "Talhão 1",
            "Talhão 4",
            "Talhão 3",
            "Sede da Fazenda"
        ]
    ],
    "total_distance": 222.60,
    "message": "Rota otimizada com sucesso!"
}
```

---

## ⚙️ Instalação  

Clone o repositório:  

```bash  
git clone https://github.com/andre-bandeli/CropPilot.git  
cd CropPilot  
```

Ambiente virtual:  
```bash  
python -m venv venv  
source venv/bin/activate  # Linux/Mac  
venv\Scripts\activate    # Windows  
```

Instale as dependências:  
```bash  
pip install -r requirements.txt  
```

Banco de dados:  
```bash  
python manage.py migrate  
```

Execute:  
```bash  
python manage.py runserver  
```

---

## 🧪 Testes  

**Via Postman:**  
- Importe a coleção `CropPilot.postman_collection.json`  
- Envie requisições para `http://localhost:8000/api/optimize/`  

**Via cURL:**  
```bash  
curl -X POST http://localhost:8000/api/optimize/ \  
-H "Content-Type: application/json" \  
-d '{"points": [{"latitude": -29.68, "longitude": -53.78}], "machine": {"capacity_kg": 1500}}'  
```

---

## 📈 Roadmap & Evolução

[ ] Implementação de restrições de Capacidade (CVRP - Capacitated Vehicle Routing Problem).

[ ] Integração com API de clima para evitar rotas em solos com alta umidade.

[ ] Interface visual com Leaflet.js para visualização dos polígonos.

---

## 🤝 Como Contribuir  
- Abra uma issue descrevendo a melhoria  
- Faça um fork do projeto  
- Crie uma branch: `git checkout -b feature/nova-funcionalidade`  
- Envie um Pull Request  

---


**CropPilot - Transformando inteligência computacional em eficiência no campo! 🚜💡**

---
> Desenvolvido por André L. Bandeli Jr – Graduando em Engenharia Agrícola (UNICAMP) | Técnico Mecatrônico (Cotuca/Unicamp).