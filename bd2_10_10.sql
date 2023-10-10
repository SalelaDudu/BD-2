-- Questão 1
select * from fire;



select sum(numero) as q,mes,state from fire
 group by mes,state
 order by q desc;


-- Questão 2

select ano, sum(numero) as q,state from fire where state = "Espirito Santo"
 group by state,ano
	order by ano asc;
    
-- Questão 3

select numero ,state, mes, ano from fire
    order by numero desc limit 5;

-- Questão 4

select avg(numero) as q, mes from fire where mes = fire.mes
	group by mes
	order by q desc;
    
-- Questão 5

select max(numero) as q ,mes,state from fire
	group by state,mes
    order by q desc;