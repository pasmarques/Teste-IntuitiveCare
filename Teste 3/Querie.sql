-- 1. Criar a estrutura da tabela para armazenar os dados
CREATE TABLE operadoras_financeiro (
    id SERIAL PRIMARY KEY,
    data DATE NOT NULL,
    reg_ans INT NOT NULL,
    cd_conta_contabil BIGINT NOT NULL,
    descricao TEXT NOT NULL,
    vl_saldo_inicial DECIMAL(15,2),
    vl_saldo_final DECIMAL(15,2)
);

-- 2. Importar os dados dos arquivos CSV (exemplo para PostgreSQL)
COPY operadoras_financeiro(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
FROM 'C:/Users/pedro/Documents/IntuitiveCare/Teste 3/1T2023/1T2023.csv' DELIMITER ';' CSV HEADER ENCODING 'LATIN1';

COPY operadoras_financeiro(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
FROM 'C:/Users/pedro/Documents/IntuitiveCare/Teste 3/2T2023/2T2023.csv' DELIMITER ';' CSV HEADER ENCODING 'LATIN1';

COPY operadoras_financeiro(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
FROM 'C:/Users/pedro/Documents/IntuitiveCare/Teste 3/3T2023/3T2023.csv' DELIMITER ';' CSV HEADER ENCODING 'LATIN1';

COPY operadoras_financeiro(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
FROM 'C:/Users/pedro/Documents/IntuitiveCare/Teste 3/4T2023/4T2023.csv' DELIMITER ';' CSV HEADER ENCODING 'LATIN1';

COPY operadoras_financeiro(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
FROM 'C:/Users/pedro/Documents/IntuitiveCare/Teste 3/1T2024/1T2024.csv' DELIMITER ';' CSV HEADER ENCODING 'LATIN1';

COPY operadoras_financeiro(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
FROM 'C:/Users/pedro/Documents/IntuitiveCare/Teste 3/2T2024/2T2024.csv' DELIMITER ';' CSV HEADER ENCODING 'LATIN1';

COPY operadoras_financeiro(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
FROM 'C:/Users/pedro/Documents/IntuitiveCare/Teste 3/3T2024/3T2024.csv' DELIMITER ';' CSV HEADER ENCODING 'LATIN1';

COPY operadoras_financeiro(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
FROM 'C:/Users/pedro/Documents/IntuitiveCare/Teste 3/4T2024/4T2024.csv' DELIMITER ';' CSV HEADER ENCODING 'LATIN1';

-- 3. Consultas analíticas

-- 3.5.1. Top 10 operadoras com maiores despesas no último trimestre (4T2024)
SELECT reg_ans, SUM(vl_saldo_final - vl_saldo_inicial) AS total_despesas
FROM operadoras_financeiro
WHERE descricao ILIKE '%EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR%'
AND data >= '2024-10-01' AND data <= '2024-12-31'
GROUP BY reg_ans
ORDER BY total_despesas DESC
LIMIT 10;

-- 3.5.2. Top 10 operadoras com maiores despesas no último ano (2024 inteiro)
SELECT reg_ans, SUM(vl_saldo_final - vl_saldo_inicial) AS total_despesas
FROM operadoras_financeiro
WHERE descricao ILIKE '%EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR%'
AND data >= '2024-01-01' AND data <= '2024-12-31'
GROUP BY reg_ans
ORDER BY total_despesas DESC
LIMIT 10;
