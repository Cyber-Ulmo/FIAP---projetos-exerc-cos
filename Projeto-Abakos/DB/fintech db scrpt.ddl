-- Gerado por Oracle SQL Developer Data Modeler 22.2.0.165.1149
--   em:        2022-11-11 19:35:01 BRT
--   site:      Oracle Database 11g
--   tipo:      Oracle Database 11g



-- predefined type, no DDL - MDSYS.SDO_GEOMETRY

-- predefined type, no DDL - XMLTYPE

CREATE TABLE t_deposito_mensal (
    t_usuário_nm_usuário VARCHAR2(30) NOT NULL,
    nr_deposito01        NUMBER,
    nr_deposito02        NUMBER,
    nr_deposito03        NUMBER
);

ALTER TABLE t_deposito_mensal ADD CONSTRAINT t_deposito_mensal_pk PRIMARY KEY ( t_usuário_nm_usuário );

CREATE TABLE t_gasto_mensal (
    t_usuário_nm_usuário VARCHAR2(30) NOT NULL,
    nr_gasto01           NUMBER,
    nr_gasto02           NUMBER,
    nr_gasto03           NUMBER
);

ALTER TABLE t_gasto_mensal ADD CONSTRAINT t_gasto_mensal_pk PRIMARY KEY ( t_usuário_nm_usuário );

CREATE TABLE t_meta (
    nr_meta01            NUMBER NOT NULL,
    nr_meta02            NUMBER,
    nr_meta03            NUMBER,
    t_usuário_nm_usuário VARCHAR2(30) NOT NULL
);

ALTER TABLE t_meta ADD CONSTRAINT t_meta_pk PRIMARY KEY ( t_usuário_nm_usuário );

CREATE TABLE t_usuário (
    nm_usuário  VARCHAR2(30) NOT NULL,
    nm_banco    VARCHAR2(30) NOT NULL,
    nr_rendames NUMBER NOT NULL
);

ALTER TABLE t_usuário ADD CONSTRAINT t_usuário_pk PRIMARY KEY ( nm_usuário );

ALTER TABLE t_deposito_mensal
    ADD CONSTRAINT t_deposito_mensal_t_usuário_fk FOREIGN KEY ( t_usuário_nm_usuário )
        REFERENCES t_usuário ( nm_usuário );

ALTER TABLE t_gasto_mensal
    ADD CONSTRAINT t_gasto_mensal_t_usuário_fk FOREIGN KEY ( t_usuário_nm_usuário )
        REFERENCES t_usuário ( nm_usuário );

ALTER TABLE t_meta
    ADD CONSTRAINT t_meta_t_usuário_fk FOREIGN KEY ( t_usuário_nm_usuário )
        REFERENCES t_usuário ( nm_usuário );



-- Relatório do Resumo do Oracle SQL Developer Data Modeler: 
-- 
-- CREATE TABLE                             4
-- CREATE INDEX                             0
-- ALTER TABLE                              7
-- CREATE VIEW                              0
-- ALTER VIEW                               0
-- CREATE PACKAGE                           0
-- CREATE PACKAGE BODY                      0
-- CREATE PROCEDURE                         0
-- CREATE FUNCTION                          0
-- CREATE TRIGGER                           0
-- ALTER TRIGGER                            0
-- CREATE COLLECTION TYPE                   0
-- CREATE STRUCTURED TYPE                   0
-- CREATE STRUCTURED TYPE BODY              0
-- CREATE CLUSTER                           0
-- CREATE CONTEXT                           0
-- CREATE DATABASE                          0
-- CREATE DIMENSION                         0
-- CREATE DIRECTORY                         0
-- CREATE DISK GROUP                        0
-- CREATE ROLE                              0
-- CREATE ROLLBACK SEGMENT                  0
-- CREATE SEQUENCE                          0
-- CREATE MATERIALIZED VIEW                 0
-- CREATE MATERIALIZED VIEW LOG             0
-- CREATE SYNONYM                           0
-- CREATE TABLESPACE                        0
-- CREATE USER                              0
-- 
-- DROP TABLESPACE                          0
-- DROP DATABASE                            0
-- 
-- REDACTION POLICY                         0
-- 
-- ORDS DROP SCHEMA                         0
-- ORDS ENABLE SCHEMA                       0
-- ORDS ENABLE OBJECT                       0
-- 
-- ERRORS                                   0
-- WARNINGS                                 0
