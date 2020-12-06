-- For sakha adikrit--vacant post id=1
--  slcvalidation ----
INSERT INTO slcvalidation 
SELECT  
ap.post, ei.document as academics, ei.board,ei.equivalance, ei.apply_post_id, ap.id,ap.vacant_post_id, ei.level
FROM 
`apply_posts` ap,`education_infos` ei
WHERE ap.id=ei.apply_post_id and ap.vacant_post_id=1 and (ei.level ="SLC" or ei.level="SEE") 

--  plus2validation--  
INSERT INTO plus2validation 
SELECT  
ap.post, ei.document as academics, ei.board,ei.equivalance, ei.apply_post_id, ap.id,ap.vacant_post_id, ei.level
FROM 
`slcvalidation` ap,`education_infos` ei
WHERE ap.id=ei.apply_post_id  and (ei.level ="+2/PCL"or ei.level="A-LeveL")

-- bachleorsvalidation---
INSERT INTO bachleorsvalidation
SELECT  Distinct 
ap.post, ei.document as academics, ei.board,ei.equivalance, ei.apply_post_id, ap.id,ap.vacant_post_id, ei.level
FROM 
`plus2validation` ap,`education_infos` ei
WHERE ap.id=ei.apply_post_id  and (ei.level ="Bachelors")



--bachleorswithgrade
INSERT INTO bachleorswithgrade
SELECT  Distinct 
ap.post, ei.document as academics, ei.board,ei.equivalance, ei.apply_post_id, ap.id,ap.vacant_post_id, ei.level,ei.grade
FROM 
`plus2validation` ap,`education_infos` ei
WHERE ap.id=ei.apply_post_id  and (ei.level ="Bachelors")

-- % to '' after bachleorsvalidation
update bachleorswithgrade set grade = replace(grade, ‘%’, ‘’) where  1

-- For sakha adikrit--

-- For sahayak Station master(सहायक स्टेसन मास्टर)vacant post id=7
-- slc validation
INSERT INTO slc_sahayak_station_master 
SELECT  
ap.post, ei.document as academics, ei.board,ei.equivalance, ei.apply_post_id, ap.id,ap.vacant_post_id, ei.level
FROM 
`apply_posts` ap,`education_infos` ei
WHERE ap.id=ei.apply_post_id and ap.vacant_post_id=7 and (ei.level ="SLC" or ei.level="SEE" or ei.level="O-Level")
-- slc validation
-- plus2validation
INSERT INTO plus2_sahayak_station_master 
SELECT  
ap.post, ei.document as academics, ei.board,ei.equivalance, ei.apply_post_id, ap.id,ap.vacant_post_id, ei.level
FROM 
`slc_sahayak_station_master` ap,`education_infos` ei
WHERE ap.id=ei.apply_post_id and ap.vacant_post_id=7 and (ei.level ="+2/PCL"or ei.level="A-LeveL")

-- plus2validation

-- sahayak Station master who have done bachleors
SELECT ap.post, ei.document as academics, ei.board,ei.equivalance, ei.apply_post_id, ap.id,ap.vacant_post_id, ei.level FROM `plus2_sahayak_station_master` ap,`education_infos` ei WHERE ap.id=ei.apply_post_id and ap.vacant_post_id=7 and (ei.level="Bachelors")
-- sahayak Station master who have done bachleors
-- For sahayak Station master(सहायक स्टेसन मास्टर)


-- For pramukh prasasan sahayak(प्रमुख प्रशासन सहायक)vacant post id=8
-- slc validation
INSERT INTO slc_pramukh_prasasan_sahayak
SELECT  
ap.post, ei.document as academics, ei.board,ei.equivalance, ei.apply_post_id, ap.id,ap.vacant_post_id, ei.level,ei.grade
FROM 
`apply_posts` ap,`education_infos` ei
WHERE ap.id=ei.apply_post_id and ap.vacant_post_id=8 and  (ei.level ="SLC" or ei.level="SEE" or ei.level="O-Level")
-- slc validation
--plus2validation
INSERT INTO plus2_pramukh_prasasan_sahayak
SELECT  
ap.post, ei.document as academics, ei.board,ei.equivalance, ei.apply_post_id, ap.id,ap.vacant_post_id, ei.level,ei.grade
FROM 
`slc_pramukh_prasasan_sahayak` ap,`education_infos` ei
WHERE ap.id=ei.apply_post_id and ap.vacant_post_id=8 and  (ei.level ="+2/PCL" or ei.level="A-LeveL")
--plus2validation
-- For pramukh prasasan sahayak(प्रमुख प्रशासन सहायक)vacant post id=8

-- For computer operator(कम्प्युटर अपरेटर)vacant post id=10
-- slc validation
INSERT INTO slc_computer_operator

SELECT  
ap.post, ei.document as academics, ei.board,ei.equivalance, ei.apply_post_id, ap.id,ap.vacant_post_id, ei.level,ei.grade
FROM 
`apply_posts` ap,`education_infos` ei
WHERE ap.id=ei.apply_post_id and ap.vacant_post_id=10 and  (ei.level ="SLC" or ei.level="SEE" or ei.level="O-Level")
-- slc validation
--plus2validation
INSERT INTO plus2_computer_operator
SELECT  
ap.post, ei.document as academics, ei.board,ei.equivalance, ei.apply_post_id, ap.id,ap.vacant_post_id, ei.level,ei.grade
FROM 
`slc_computer_operator` ap,`education_infos` ei
WHERE ap.id=ei.apply_post_id and ap.vacant_post_id=10 and  (ei.level ="+2/PCL" or ei.level="A-LeveL")
--plus2validation
-- For computer operator(कम्प्युटर अपरेटर)vacant post id=10

-- For TTE(टि.टि.ई.)vacant post id=20
-- slc validation
    INSERT INTO slc_TTE
    SELECT  
    ap.post, ei.document as academics, ei.board,ei.equivalance, ei.apply_post_id, ap.id,ap.vacant_post_id, ei.level,ei.grade
    FROM 
    `apply_posts` ap,`education_infos` ei
    WHERE ap.id=ei.apply_post_id and ap.vacant_post_id=20 and  (ei.level ="SLC" or ei.level="SEE" or ei.level="O-Level")
-- slc validation
-- For TTE(टि.टि.ई.)vacant post id=20

-- For lekhapal(लेखापाल)vacant post id=9
-- slc validation
    INSERT INTO slc_lekhapal
    SELECT  Distinct
    ap.post, ei.document as academics, ei.board,ei.equivalance, ei.apply_post_id, ap.id,ap.vacant_post_id, ei.level,ei.grade
    FROM 
    `apply_posts` ap,`education_infos` ei
    WHERE ap.id=ei.apply_post_id and ap.vacant_post_id=9 and  (ei.level ="SLC" or ei.level="SEE" or ei.level="O-Level")
-- slc validation
--plus2validation
INSERT INTO plus2_lekhapal
SELECT  Distinct
ap.post, ei.document as academics, ei.board,ei.equivalance, ei.apply_post_id, ap.id,ap.vacant_post_id, ei.level,ei.grade
FROM 
`slc_lekhapal` ap,`education_infos` ei
WHERE ap.id=ei.apply_post_id and ap.vacant_post_id=9 and  (ei.level ="+2/PCL" or ei.level="A-LeveL")
--plus2validation
-- For lekhapal(लेखापाल)vacant post id=9


-- For station master(स्टेसन मास्टर)vacant post id=3
-- slc validation
    INSERT INTO slc_station_master
    SELECT  Distinct
    ap.post, ei.document as academics, ei.board,ei.equivalance, ei.apply_post_id, ap.id,ap.vacant_post_id, ei.level,ei.grade
    FROM 
    `apply_posts` ap,`education_infos` ei
    WHERE ap.id=ei.apply_post_id and ap.vacant_post_id=3 and  (ei.level ="SLC" or ei.level="SEE" or ei.level="O-Level")
-- slc validation
--plus2validation
INSERT INTO plus2_station_master
SELECT  Distinct
 ap.post, ei.document as academics, ei.board,ei.equivalance, ei.apply_post_id, ap.id,ap.vacant_post_id, ei.level,ei.grade
FROM 
`slc_station_master` ap,`education_infos` ei
WHERE ap.id=ei.apply_post_id and ap.vacant_post_id=3 and  (ei.level ="+2/PCL" or ei.level="A-LeveL")
--plus2validation
-- Bachleors validation
INSERT INTO bachleors_station_master
SELECT  Distinct
ap.post, ei.document as academics, ei.board,ei.equivalance, ei.apply_post_id, ap.id,ap.vacant_post_id, ei.level,ei.grade
FROM 
`plus2_station_master` ap,`education_infos` ei
WHERE ap.id=ei.apply_post_id and ap.vacant_post_id=3 and  (ei.level ="Bachelors")
-- Bachleors validation
-- For station master(स्टेसन मास्टर)vacant post id=3


-- For cashier(क्यासियर)vacant post id=11
-- slc validation
    INSERT INTO slc_cashier
    SELECT  Distinct
    ap.post, ei.document as academics, ei.board,ei.equivalance, ei.apply_post_id, ap.id,ap.vacant_post_id, ei.level,ei.grade
    FROM 
    `apply_posts` ap,`education_infos` ei
    WHERE ap.id=ei.apply_post_id and ap.vacant_post_id=11 and  (ei.level ="SLC" or ei.level="SEE" or ei.level="O-Level")
-- slc validation
-- For station master(स्टेसन मास्टर)vacant post id=11
-- mec
-- elec
-- elec_and_com
-- For sub Engineer(सव इन्जीनियर)vacant post id=4
-- slc validation
    INSERT INTO slc_sub_engineer_mec
    SELECT  Distinct
    ap.post, ei.document as academics, ei.board,ei.equivalance, ei.apply_post_id, ap.id,ap.vacant_post_id, ei.level,ei.grade
    FROM 
    `apply_posts` ap,`education_infos` ei
    WHERE ap.id=ei.apply_post_id and ap.vacant_post_id=4 and  (ei.level ="SLC" or ei.level="SEE" or ei.level="O-Level")
-- slc validation
--plus2validation
INSERT INTO plus2_sub_engineer_mec
SELECT  Distinct
 ap.post, ei.document as academics, ei.board,ei.equivalance, ei.apply_post_id, ap.id,ap.vacant_post_id, ei.level,ei.grade
FROM 
`slc_sub_engineer_mec` ap,`education_infos` ei
WHERE ap.id=ei.apply_post_id and ap.vacant_post_id=4 and  (ei.level ="+2/PCL" or ei.level="A-LeveL")
--plus2validation
-- For sub Engineer(सव इन्जीनियर)vacant post id=4

-- For sub Engineer_elec(सव इन्जीनियर)vacant post id=5
-- slc validation
    INSERT INTO slc_sub_engineer_elec
    SELECT  Distinct
    ap.post, ei.document as academics, ei.board,ei.equivalance, ei.apply_post_id, ap.id,ap.vacant_post_id, ei.level,ei.grade
    FROM 
    `apply_posts` ap,`education_infos` ei
    WHERE ap.id=ei.apply_post_id and ap.vacant_post_id=5 and  (ei.level ="SLC" or ei.level="SEE" or ei.level="O-Level")
-- slc validation
--plus2validation
INSERT INTO plus2_sub_engineer_elec
SELECT  Distinct
 ap.post, ei.document as academics, ei.board,ei.equivalance, ei.apply_post_id, ap.id,ap.vacant_post_id, ei.level,ei.grade
FROM 
`slc_sub_engineer_elec` ap,`education_infos` ei
WHERE ap.id=ei.apply_post_id and ap.vacant_post_id=5 and  (ei.level ="+2/PCL" or ei.level="A-LeveL")
--plus2validation
-- For sub Engineer_elec(सव इन्जीनियर)vacant post id=5

-- For sub Engineer_elec(सव इन्जीनियर)vacant post id=6
-- slc validation
    INSERT INTO slc_sub_engineer_elec_com
    SELECT  Distinct
    ap.post, ei.document as academics, ei.board,ei.equivalance, ei.apply_post_id, ap.id,ap.vacant_post_id, ei.level,ei.grade
    FROM 
    `apply_posts` ap,`education_infos` ei
    WHERE ap.id=ei.apply_post_id and ap.vacant_post_id=6 and  (ei.level ="SLC" or ei.level="SEE" or ei.level="O-Level")
-- slc validation
--plus2validation
INSERT INTO plus2_sub_engineer_elec_com
SELECT  Distinct
 ap.post, ei.document as academics, ei.board,ei.equivalance, ei.apply_post_id, ap.id,ap.vacant_post_id, ei.level,ei.grade
FROM 
`slc_sub_engineer_elec_com` ap,`education_infos` ei
WHERE ap.id=ei.apply_post_id and ap.vacant_post_id=6 and  (ei.level ="+2/PCL" or ei.level="A-LeveL")
--plus2validation
-- For sub Engineer_elec(सव इन्जीनियर)vacant post id=6

-- For track_nirixhak(ट्रयाक निरीक्षक (PWI))vacant post id=14
-- slc validation
    INSERT INTO track_nirixhak
    SELECT  Distinct
    ap.post, ei.document as academics, ei.board,ei.equivalance, ei.apply_post_id, ap.id,ap.vacant_post_id, ei.level,ei.grade
    FROM 
    `apply_posts` ap,`education_infos` ei
    WHERE ap.id=ei.apply_post_id and ap.vacant_post_id=14 and  (ei.level ="SLC" or ei.level="SEE" or ei.level="O-Level")
-- slc validation
-- For track_nirixhak(ट्रयाक निरीक्षक (PWI))vacant post id=14

-- For foreman(फोरम्यान)vacant post id=15
-- slc validation
    INSERT INTO slc_foreman
    SELECT  Distinct
    ap.post, ei.document as academics, ei.board,ei.equivalance, ei.apply_post_id, ap.id,ap.vacant_post_id, ei.level,ei.grade
    FROM 
    `apply_posts` ap,`education_infos` ei
    WHERE ap.id=ei.apply_post_id and ap.vacant_post_id=15 and  (ei.level ="SLC" or ei.level="SEE" or ei.level="O-Level")
-- slc validation
-- For foreman(फोरम्यान)vacant post id=15

-- For electrician(इलेक्ट्रिसियन)vacant post id=16
-- slc validation
    INSERT INTO slc_electrician
    SELECT  Distinct
    ap.post, ei.document as academics, ei.board,ei.equivalance, ei.apply_post_id, ap.id,ap.vacant_post_id, ei.level,ei.grade
    FROM 
    `apply_posts` ap,`education_infos` ei
    WHERE ap.id=ei.apply_post_id and ap.vacant_post_id=16 and  (ei.level ="SLC" or ei.level="SEE" or ei.level="O-Level")
-- slc validation
-- For electrician(इलेक्ट्रिसियन)vacant post id=16


-- For estm(अमिन)vacant post id=18
-- slc validation
    INSERT INTO slc_estm
    SELECT  Distinct
    ap.post, ei.document as academics, ei.board,ei.equivalance, ei.apply_post_id, ap.id,ap.vacant_post_id, ei.level,ei.grade
    FROM 
    `apply_posts` ap,`education_infos` ei
    WHERE ap.id=ei.apply_post_id and ap.vacant_post_id=18 and  (ei.level ="SLC" or ei.level="SEE" or ei.level="O-Level")
-- slc validation
-- For amin(अमिन)vacant post id=18

-- For rail guard(रेल गार्ड)vacant post id=19
-- slc validation
    INSERT INTO slc_rail_guard
    SELECT  Distinct
    ap.post, ei.document as academics, ei.board,ei.equivalance, ei.apply_post_id, ap.id,ap.vacant_post_id, ei.level,ei.grade
    FROM 
    `apply_posts` ap,`education_infos` ei
    WHERE ap.id=ei.apply_post_id and ap.vacant_post_id=19 and  (ei.level ="SLC" or ei.level="SEE" or ei.level="O-Level")
-- slc validation
-- For rail guard(रेल गार्ड)vacant post id=19


-- For gang_man_incharge(ग्यांगम्यान इन्चार्ज)vacant post id=21
-- slc validation
    INSERT INTO slc_gang_man_incharge
    SELECT  Distinct
    ap.post, ei.document as academics, ei.board,ei.equivalance, ei.apply_post_id, ap.id,ap.vacant_post_id, ei.level,ei.grade
    FROM 
    `apply_posts` ap,`education_infos` ei
    WHERE ap.id=ei.apply_post_id and ap.vacant_post_id=21 and  (ei.level ="SLC" or ei.level="SEE" or ei.level="O-Level")
-- slc validation
-- For gang_man_incharge(ग्यांगम्यान इन्चार्ज)vacant post id=21

-- For keyman(ग्यांगम्यान इन्चार्ज)vacant post id=22
-- slc validation
    INSERT INTO slc_keyman
    SELECT  Distinct
    ap.post, ei.document as academics, ei.board,ei.equivalance, ei.apply_post_id, ap.id,ap.vacant_post_id, ei.level,ei.grade
    FROM 
    `apply_posts` ap,`education_infos` ei
    WHERE ap.id=ei.apply_post_id and ap.vacant_post_id=22 and  (ei.level ="SLC" or ei.level="SEE" or ei.level="O-Level")
-- slc validation
-- For keyman(ग्यांगम्यान इन्चार्ज)vacant post id=22

-- For kanun_adikrit(कानून अधिकृत)vacant post id=2
-- slc validation
    INSERT INTO slc_kanun_adikrit
    SELECT  Distinct
    ap.post, ei.document as academics, ei.board,ei.equivalance, ei.apply_post_id, ap.id,ap.vacant_post_id, ei.level,ei.grade
    FROM 
    `apply_posts` ap,`education_infos` ei
    WHERE ap.id=ei.apply_post_id and ap.vacant_post_id=2 and  (ei.level ="SLC" or ei.level="SEE" or ei.level="O-Level")
-- slc validation
--plus2validation
INSERT INTO plus2_kanun_adikrit
SELECT  Distinct
 ap.post, ei.document as academics, ei.board,ei.equivalance, ei.apply_post_id, ap.id,ap.vacant_post_id, ei.level,ei.grade
FROM 
`slc_kanun_adikrit` ap,`education_infos` ei
WHERE ap.id=ei.apply_post_id and ap.vacant_post_id=2 and  (ei.level ="+2/PCL" or ei.level="A-LeveL")
--plus2validation

-- Bachleors validation
INSERT INTO bachleors_kanun_adikrit
SELECT  Distinct
ap.post, ei.document as academics, ei.board,ei.equivalance, ei.apply_post_id, ap.id,ap.vacant_post_id, ei.level,ei.grade
FROM 
`plus2_kanun_adikrit` ap,`education_infos` ei
WHERE ap.id=ei.apply_post_id and ap.vacant_post_id=2 and  (ei.level ="Bachelors")
-- Bachleors validation

-- For kanun_adikrit(कानून अधिकृत)vacant post id=2


-- ticket bikreta sahayek (vacant post id=12)
-- slc validation
    INSERT INTO slc_ticket_bikreta_sahayek
    SELECT  Distinct
    ap.post, ei.document as academics, ei.board,ei.equivalance, ei.apply_post_id, ap.id,ap.vacant_post_id, ei.level,ei.grade
    FROM 
    `apply_posts` ap,`education_infos` ei
    WHERE ap.id=ei.apply_post_id and ap.vacant_post_id=12 and  (ei.level ="SLC" or ei.level="SEE" or ei.level="O-Level")
-- slc validation
--plus2validation
INSERT INTO plus2_ticket_bikreta_sahayek
SELECT  Distinct
 ap.post, ei.document as academics, ei.board,ei.equivalance, ei.apply_post_id, ap.id,ap.vacant_post_id, ei.level,ei.grade
FROM 
`slc_ticket_bikreta_sahayek` ap,`education_infos` ei
WHERE ap.id=ei.apply_post_id and ap.vacant_post_id=12 and  (ei.level ="+2/PCL" or ei.level="A-LeveL")
--plus2validation

-- ticket bikreta sahayek (vacant post id=12)


















-- :TODO:Missing query
-- ticket bikreta sahayek (vacant post id=12)






-- -- Function
-- CREATE FUNCTION REDUCE ( starting_value INT )
-- RETURNS INT

-- BEGIN

--    DECLARE income INT;

--    SET income = 0;

--    label1: WHILE income <= 3000 DO
--      SET income = income + starting_value;
--    END WHILE label1;

--    RETURN income;

-- END;






