# Monitoramento remoto da qualidade da água: Armazenamento e recuperação de dados IoT em nuvem.

## O Projeto


Este projeto tem como objetivo a criação de um protótipo utilizando arduino e sensores cujo objetivo é por meio de uma solução IoT monitorar a qualidade da água nas bacias amazônicas. 

![image](https://user-images.githubusercontent.com/83120884/226697247-1bc982b3-a211-42cb-9664-0d89fb575f66.png)


Arquitetura básica do projeto: 

![image](https://user-images.githubusercontent.com/83120884/226697851-d4be8f0a-fc4d-4b7d-ba6f-67f96fed112e.png)

## Authors

- [@diogosm](https://www.github.com/diogosm)
- [@Mateuxx](https://github.com/Mateuxx)

## Firebase Para Armazanenameto Dados

Como Data server foi optado por esse projeto o Firebase, pela sua facilidade de integração com app android e até certa facilidade de integração com aplicações web. 

Os dados são captados pelos sensores ( neste projeto são utilizados os sensores de: temperatura, turbidez,  PH e condutividade) enviados para o Raspberry Pi e Lora(Gateway). Com isso os dados são tratados por meio de um script em python que armazena esses dados em um banco utilizando o SQLITE3  para facilitação de formatação dos dados ao alimentar o RealTime Database.

Após a inserção no banco, Para facilitar a inserção da ultima marcação dos sensores (last Record) no firebase os dados são enviados ao Realtime database que possui a seguinte Estrutura :

## Estrutura do Realtime Firebase
```

| — - PAi 
      | — — Last Record (PH, TDS, Temperatura, Turbidez) 
      | — — Sensor
                  | — — PH
                              | — — Leitura 1 
                              | — — …..
                              | — — Leitura N
                  | — — TDS
                              | — — Leitura 1 
                              | — — …..
                              | — — Leitura N
                  | — — Temperatura
                              | — — Leitura 1 
                              | — — …..
                              | — — Leitura N
                  | — —  Turbidez
                              | — — Leitura 1 
                              | — — …..
                              | — — Leitura N
```
 
# Diagrama de funcionamento Geral (Firebase) 

![testeee (1)](https://user-images.githubusercontent.com/83120884/226636490-24541005-9e21-4964-be33-fd47dcbfef80.jpg)
