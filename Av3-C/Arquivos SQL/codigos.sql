select * from livro;
select * from livro_log;

-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
-- comando para inserção
DELIMITER //

CREATE PROCEDURE cadastro (
    IN n_id INT,
    IN n_nome VARCHAR(120),
    IN n_genero VARCHAR(120),
    IN n_autor VARCHAR(120)
)
BEGIN
    DECLARE versao_a INT;

    -- Encontra a versão atual do livro, se existir
    SELECT MAX(versao) INTO versao_a FROM livro WHERE id = n_id;

    -- Se o livro existe, move para livro_log
    IF versao_a IS NOT NULL THEN
        INSERT INTO livro_log (id, versao, nome, genero, autor)
        SELECT id, versao, nome, genero, autor
        FROM livro WHERE id = n_id;

	-- Remove todas as versões anteriores do livro na tabela principal
        DELETE FROM livro WHERE id = n_id;
    END IF;

    -- Insere o novo registro na tabela principal
    INSERT INTO livro (id, versao, nome, genero, autor)
    VALUES (n_id, IFNULL(versao_a, 0) + 1, n_nome, n_genero, n_autor);
END //

-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
-- comando para atualização
DELIMITER //

CREATE PROCEDURE Att_Livro (
    IN n_id INT,
    IN n_nome VARCHAR(120),
    IN n_genero VARCHAR(120),
    IN n_autor VARCHAR(120)
)
BEGIN
    DECLARE versao_a INT;

    -- Encontra a versão atual do livro, se existir
    SELECT MAX(versao) INTO versao_a FROM livro WHERE id = n_id;

    -- Mover a versão atual para log
    IF versao_a IS NOT NULL THEN
        INSERT INTO livro_log (id, versao, nome, genero, autor)
        SELECT id, versao, nome, genero, autor
        FROM livro WHERE id = n_id;
    END IF;

    -- Atualizar o registro na tabela principal
    UPDATE livro
    SET nome = n_nome, genero = n_genero, autor = n_autor
    WHERE id = n_id;

    -- Incrementar a versão na tabela principal
    UPDATE livro
    SET versao = IFNULL(versao_a, 0) + 1
    WHERE id = n_id AND versao = versao_a;
END //

DELIMITER ;

-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
-- comando para exclusão
DELIMITER //

CREATE PROCEDURE excluir (
    IN n_id INT
)
BEGIN
    DECLARE versao_a INT;

    -- Encontra a versão atual do livro, se existir
    SELECT COALESCE(MAX(versao), 0) INTO versao_a FROM livro WHERE id = n_id;

    -- Mover o registro para livro_log antes de excluí-lo
    INSERT INTO livro_log (id, versao, nome, genero, autor)
    SELECT id, versao_a, nome, genero, autor
    FROM livro WHERE id = n_id AND versao = versao_a;

    -- Excluir o registro da tabela principal
    DELETE FROM livro WHERE id = n_id AND versao = versao_a;
END //

DELIMITER ;

-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 

CALL cadastro(1,'Harry Potter e a pedra filosoal','ficção','J. K. Howling');
CALL cadastro(2,'O universo em uma casca de noz','não-ficção','Stephen Hawking');
CALL cadastro(3,'O mundo asosmbrado pelos demônios','não-ficção','Carl Sagan');
CALL cadastro(4,'As crônicas de gelo e fogo','ficção','R. R. Martin');
CALL cadastro(5,'Sapiens: uma breve história da humanidade','não-ficção','Yuval Harari');


CALL Att_Livro(2, 'Uma breve história do tempo', 'não-ficção', 'Stephen Hawking');


CALL excluir(2);
