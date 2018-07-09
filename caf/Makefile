ECHO_SUCCESS=@echo " \033[1;32m✔\033[0m  "

all: install download_commune data_commune merging

install:
	pip install -r requirements.txt
	@rm -rf source
	@mkdir source
	@rm -rf data
	@mkdir data

download_commune:
	# DependancePrestaCom : http://data.caf.fr/dataset/indicateur-sur-la-part-des-prestations-dans-les-ressources-des-foyers-allocataires-par-commune
	@wget -O source/DependancePrestaCom2009.csv http://data.caf.fr/dataset/87fd090b-956a-4d57-b8eb-c03b08f22b4c/resource/75189698-90ce-44f7-aa4f-aa4e23161010/download/DependancePrestaCom2009.csv
	@wget -O source/DependancePrestaCom2010.csv http://data.caf.fr/dataset/87fd090b-956a-4d57-b8eb-c03b08f22b4c/resource/6a10f992-700b-4b91-992a-5bf8c7fe5eba/download/DependancePrestaCom2010.csv
	@wget -O source/DependancePrestaCom2011.csv http://data.caf.fr/dataset/87fd090b-956a-4d57-b8eb-c03b08f22b4c/resource/08afcec2-308c-49fd-b549-a3a7256b49c8/download/DependancePrestatCom2011.csv
	@wget -O source/DependancePrestaCom2012.csv http://data.caf.fr/dataset/87fd090b-956a-4d57-b8eb-c03b08f22b4c/resource/8e08685c-1c2d-47dd-be59-c88447c0f7d5/download/DependancePrestaCom2012.csv
	@wget -O source/DependancePrestaCom2013.csv http://data.caf.fr/dataset/87fd090b-956a-4d57-b8eb-c03b08f22b4c/resource/cf0c4874-7490-4eab-a3cd-db5c33ff9f72/download/DependanceprestaCom2013.csv
	@wget -O source/DependancePrestaCom2014.csv http://data.caf.fr/dataset/87fd090b-956a-4d57-b8eb-c03b08f22b4c/resource/f6cd0adb-2cc8-4c2f-8603-235b11c205ac/download/DependancePrestaCom2014.csv
	@wget -O source/DependancePrestaCom2015.csv http://data.caf.fr/dataset/87fd090b-956a-4d57-b8eb-c03b08f22b4c/resource/5670b984-c42c-4664-9a42-f81da4738b9a/download/TauxEffortCom2015.csv
	

	# BasrevnuCom : http://data.caf.fr/dataset/beneficiaire-bas-revenus
	@wget -O source/BasrevenuCom2009.csv http://data.caf.fr/dataset/79250fae-53f6-4d7c-91da-218e79bdcb60/resource/c51b0621-9b2a-4031-9859-553b06731ec3/download/BasrevenuCom2009.csv
	@wget -O source/BasrevenuCom2010.csv http://data.caf.fr/dataset/79250fae-53f6-4d7c-91da-218e79bdcb60/resource/4a9e6c6d-0f36-4e1c-897a-e7801a0b35d0/download/BasrevenuCom2010.csv
	@wget -O source/BasrevenuCom2011.csv http://data.caf.fr/dataset/79250fae-53f6-4d7c-91da-218e79bdcb60/resource/29796950-288c-4d25-b3d5-d365dd14a712/download/BasrevenuCom2011.csv
	@wget -O source/BasrevenuCom2012.csv http://data.caf.fr/dataset/79250fae-53f6-4d7c-91da-218e79bdcb60/resource/cbb003eb-46da-4ce2-98ad-e617dfef4e2b/download/BasrevenuCom2012.csv
	@wget -O source/BasrevenuCom2013.csv http://data.caf.fr/dataset/79250fae-53f6-4d7c-91da-218e79bdcb60/resource/c45d1b54-17be-4a80-89a0-5ec832e82599/download/BasrevenuCom2013.csv
	@wget -O source/BasrevenuCom2014.csv http://data.caf.fr/dataset/79250fae-53f6-4d7c-91da-218e79bdcb60/resource/a2e0ac46-d4ac-42cc-a28c-bd6b067004b0/download/BasrevenuCom2014.csv
	@wget -O source/BasrevenuCom2015.csv http://data.caf.fr/dataset/79250fae-53f6-4d7c-91da-218e79bdcb60/resource/2f5e861c-0626-4e91-8745-0a5998b4aca7/download/BasrevenuCom2015.csv

	# NIVCOMTOTAL2009 : http://data.caf.fr/dataset/population-des-foyers-allocataires-par-commune
	@wget -O source/NivComTotal2009.csv http://data.caf.fr/dataset/32cc7f8a-f15a-4372-b862-dcb247b1bfb6/resource/dfc08b49-20fe-4a58-8e3f-96cfa3f02e2c/download/NIVCOMTOTAL2009.csv
	@wget -O source/NivComTotal2010.csv http://data.caf.fr/dataset/32cc7f8a-f15a-4372-b862-dcb247b1bfb6/resource/1327c4f0-f417-4513-b908-18e90a543b40/download/NIVCOMTOTAL2010.csv
	@wget -O source/NivComTotal2011.csv http://data.caf.fr/dataset/32cc7f8a-f15a-4372-b862-dcb247b1bfb6/resource/25a1ee5c-d4c5-4bbf-a3a4-74e107e222a5/download/NIVCOMTOTAL2011.csv
	@wget -O source/NivComTotal2012.csv http://data.caf.fr/dataset/32cc7f8a-f15a-4372-b862-dcb247b1bfb6/resource/a4e53a7b-c489-44f2-90a0-2e0ca375932b/download/NIVCOMTOTAL2012.csv
	@wget -O source/NivComTotal2013.csv http://data.caf.fr/dataset/32cc7f8a-f15a-4372-b862-dcb247b1bfb6/resource/0390c41c-6f07-4a34-b9f6-9ecd8c7335d6/download/NIVCOMTOTAL2013.csv
	@wget -O source/NivComTotal2014.csv http://data.caf.fr/dataset/32cc7f8a-f15a-4372-b862-dcb247b1bfb6/resource/928c52da-21ef-49be-88b6-0835b5fb40ec/download/NIVCOMTOTAL2014.csv
	@wget -O source/NivComTotal2015.csv http://data.caf.fr/dataset/32cc7f8a-f15a-4372-b862-dcb247b1bfb6/resource/6ca79db1-8fd8-4468-bddc-6da139e8bc2f/download/NIVCOMTOTAL2015.csv

	# ConfigFamiliale : http://data.caf.fr/dataset/repartition-des-foyers-allocataires-selon-le-type-de-famille-par-commune
	@wget -O source/ConfigFamiliale2009.csv	http://data.caf.fr/dataset/55b512d5-fc90-41ff-9908-47b41d0599a3/resource/59ea1a6a-a02b-4b3d-bfed-ccf17db2048c/download/configfamiliale2009.csv
	@wget -O source/ConfigFamiliale2010.csv	http://data.caf.fr/dataset/55b512d5-fc90-41ff-9908-47b41d0599a3/resource/64f6bf65-df32-470d-b35c-c4954336b6de/download/configfamiliale2010.csv
	@wget -O source/ConfigFamiliale2011.csv	http://data.caf.fr/dataset/55b512d5-fc90-41ff-9908-47b41d0599a3/resource/97528a0a-658d-48d2-9229-cf5b4f3ad85b/download/configfamiliale2011.csv
	@wget -O source/ConfigFamiliale2012.csv	http://data.caf.fr/dataset/55b512d5-fc90-41ff-9908-47b41d0599a3/resource/051439cc-bbd1-4500-bc56-f067bf4a2a00/download/configfamiliale2012.csv
	@wget -O source/ConfigFamiliale2013.csv	http://data.caf.fr/dataset/55b512d5-fc90-41ff-9908-47b41d0599a3/resource/e8dfc5a1-1589-4a8b-a006-b77d7ad8d3d2/download/configfamiliale2013.csv
	@wget -O source/ConfigFamiliale2014.csv	http://data.caf.fr/dataset/55b512d5-fc90-41ff-9908-47b41d0599a3/resource/12762e3a-f4e1-4b64-8956-7cdedf7e56e8/download/configfamiliale2014.csv
	@wget -O source/ConfigFamiliale2015.csv	http://data.caf.fr/dataset/55b512d5-fc90-41ff-9908-47b41d0599a3/resource/50224e63-cd95-4189-85cf-000da4fc11e8/download/configfamiliale2015.csv

	# TrancheAge : http://data.caf.fr/dataset/denombrement-et-repartition-des-foyers-allocataires-selon-l-age-du-responsable
	@wget -O source/TrancheAge2009.csv	http://data.caf.fr/dataset/d52a5176-195f-47c0-a851-b652e1d2875c/resource/3b326055-b1b5-4aa3-a4d2-18e895cb7e7d/download/trancheage2009.csv
	@wget -O source/TrancheAge2010.csv	http://data.caf.fr/dataset/d52a5176-195f-47c0-a851-b652e1d2875c/resource/8137ac83-32ca-48e4-a23e-d8f6263601fc/download/trancheage2010.csv
	@wget -O source/TrancheAge2011.csv	http://data.caf.fr/dataset/d52a5176-195f-47c0-a851-b652e1d2875c/resource/02dc20f2-3a3d-4272-9893-07912fe563fd/download/trancheage2011.csv
	@wget -O source/TrancheAge2012.csv	http://data.caf.fr/dataset/d52a5176-195f-47c0-a851-b652e1d2875c/resource/0f9dd215-eb6d-4479-90e0-0b0d951d5dec/download/trancheage2012.csv
	@wget -O source/TrancheAge2013.csv	http://data.caf.fr/dataset/d52a5176-195f-47c0-a851-b652e1d2875c/resource/a6283267-9635-4452-b30e-35fe8a5cdbe2/download/trancheage2013.csv
	@wget -O source/TrancheAge2014.csv	http://data.caf.fr/dataset/d52a5176-195f-47c0-a851-b652e1d2875c/resource/b46e67ea-66f9-4855-bc01-70690c1809dd/download/trancheage2014.csv
	@wget -O source/TrancheAge2015.csv	http://data.caf.fr/dataset/d52a5176-195f-47c0-a851-b652e1d2875c/resource/7fbaf1b1-3b31-4fbb-bfbb-c1a897afd80b/download/trancheage2015.csv

	# LOGCom : http://data.caf.fr/dataset/population-des-foyers-allocataires-percevant-une-aide-personnelle-au-logement
	@wget -O source/LOGCom2009.csv	http://data.caf.fr/dataset/1263e313-9bb0-417d-bb88-1488b6993ae8/resource/e8d57800-dd95-4221-b4d8-2044ba67cbcb/download/LOGCom2009.csv
	@wget -O source/LOGCom2010.csv	http://data.caf.fr/dataset/1263e313-9bb0-417d-bb88-1488b6993ae8/resource/6108a4d5-26e8-4f25-9f49-6a8da58ea6ae/download/LOGCom2010.csv
	@wget -O source/LOGCom2011.csv	http://data.caf.fr/dataset/1263e313-9bb0-417d-bb88-1488b6993ae8/resource/5867d5ab-190d-40c8-8f4d-b7eb9dc1fc8e/download/LOGCom2011.csv
	@wget -O source/LOGCom2012.csv	http://data.caf.fr/dataset/1263e313-9bb0-417d-bb88-1488b6993ae8/resource/8566dd5b-b9db-4e67-89a1-c10e62b703a8/download/LOGCom2012.csv
	@wget -O source/LOGCom2013.csv	http://data.caf.fr/dataset/1263e313-9bb0-417d-bb88-1488b6993ae8/resource/21eab4ce-9ad3-4346-8efe-cb994f2a7011/download/LOGCom2013.csv
	@wget -O source/LOGCom2014.csv	http://data.caf.fr/dataset/1263e313-9bb0-417d-bb88-1488b6993ae8/resource/37ba7456-0996-4c95-ba28-38f079d25d86/download/LOGCom2014.csv
	@wget -O source/LOGCom2015.csv	http://data.caf.fr/dataset/1263e313-9bb0-417d-bb88-1488b6993ae8/resource/e8358acd-bb66-4305-8af1-a645f70c3bc1/download/LOGCom2015.csv

	# PAJECom : http://data.caf.fr/dataset/foyers-allocataires-percevant-la-prestation-d-accueil-du-jeune-enfant-paje-par-commune
	@wget -O source/PajeCom2009.csv	http://data.caf.fr/dataset/23f79fd1-a59c-4a9a-91e5-717f126cb166/resource/41936fac-2bb5-4f64-8670-1286467fa306/download/PAJECom2009.csv
	@wget -O source/PajeCom2010.csv	http://data.caf.fr/dataset/23f79fd1-a59c-4a9a-91e5-717f126cb166/resource/d49e20a3-d3e8-4a3d-a239-fed7c2a00da6/download/PAJECom2010.csv
	@wget -O source/PajeCom2011.csv	http://data.caf.fr/dataset/23f79fd1-a59c-4a9a-91e5-717f126cb166/resource/06cec282-cdf6-40a7-8e26-ba611eb71ea6/download/PAJECom2011.csv
	@wget -O source/PajeCom2012.csv	http://data.caf.fr/dataset/23f79fd1-a59c-4a9a-91e5-717f126cb166/resource/d0903f8c-027a-4a06-963d-f56d93e84c4a/download/PAJECom2012.csv
	@wget -O source/PajeCom2013.csv	http://data.caf.fr/dataset/23f79fd1-a59c-4a9a-91e5-717f126cb166/resource/05152e2d-0d49-4245-8b41-4c4be74a6226/download/PAJECom2013.csv
	@wget -O source/PajeCom2014.csv	http://data.caf.fr/dataset/23f79fd1-a59c-4a9a-91e5-717f126cb166/resource/cc73587b-8e69-4c42-90aa-488b9ef168dd/download/PAJECom2014.csv
	@wget -O source/PajeCom2015.csv	http://data.caf.fr/dataset/23f79fd1-a59c-4a9a-91e5-717f126cb166/resource/823ab28e-2e8a-4569-8cd7-0f0dc441dedb/download/PAJECom2015.csv


	# RSAPersCom : http://data.caf.fr/dataset/population-des-foyers-allocataires-percevant-le-revenu-de-solidarite
	@wget -O source/RsaPersCom2009.csv	http://data.caf.fr/dataset/6b811c7a-6868-4223-bd93-ffaf95314c10/resource/040aeb4e-04ed-4d84-9086-072b4efedb54/download/RSAPersCom2009.csv
	@wget -O source/RsaPersCom2010.csv	http://data.caf.fr/dataset/6b811c7a-6868-4223-bd93-ffaf95314c10/resource/a6fb1025-4d77-4b45-bf30-75ee666d15fb/download/RSAPersCom2010.csv
	@wget -O source/RsaPersCom2011.csv	http://data.caf.fr/dataset/6b811c7a-6868-4223-bd93-ffaf95314c10/resource/e64497fd-f625-48c0-91be-9adfdaa49e11/download/RSAPersCom2011.csv
	@wget -O source/RsaPersCom2012.csv	http://data.caf.fr/dataset/6b811c7a-6868-4223-bd93-ffaf95314c10/resource/3811040d-ea31-436f-9f0d-04bb19c91fb8/download/RSAPersCom2012.csv
	@wget -O source/RsaPersCom2013.csv	http://data.caf.fr/dataset/6b811c7a-6868-4223-bd93-ffaf95314c10/resource/50b1afd9-d1ea-4f09-a54f-6634a9cbd9d0/download/RSAPersCom2013.csv
	@wget -O source/RsaPersCom2014.csv	http://data.caf.fr/dataset/6b811c7a-6868-4223-bd93-ffaf95314c10/resource/bdd7ad3d-5f1f-42a0-a351-9bd46c883418/download/RSAPersCom2014.csv
	@wget -O source/RsaPersCom2015.csv	http://data.caf.fr/dataset/6b811c7a-6868-4223-bd93-ffaf95314c10/resource/2ed80aaa-5d4b-4b2c-9716-9b79ff3ae65a/download/RSAPersCom2015.csv

	# AAHCom : http://data.caf.fr/dataset/personnes-ayant-un-droit-versable-a-l-allocation-aux-adultes-handicapes
	@wget -O source/AAHCom2009.csv	http://data.caf.fr/dataset/c7490d25-8907-4080-b638-d1d43b33e37f/resource/79177257-e87f-4c74-b6f1-5c9f9bfd8f31/download/AAHCom2009.csv
	@wget -O source/AAHCom2010.csv	http://data.caf.fr/dataset/c7490d25-8907-4080-b638-d1d43b33e37f/resource/6faeb068-5c12-46de-a696-6faacb2e1fb3/download/AAHCom2010.csv
	@wget -O source/AAHCom2011.csv	http://data.caf.fr/dataset/c7490d25-8907-4080-b638-d1d43b33e37f/resource/ef06d897-a3e6-49e9-9663-6c8e3b41e439/download/AAHCom2011.csv
	@wget -O source/AAHCom2012.csv	http://data.caf.fr/dataset/c7490d25-8907-4080-b638-d1d43b33e37f/resource/01308b3a-097e-4c5d-9c7c-60705d5c6de7/download/AAHCom2012.csv
	@wget -O source/AAHCom2013.csv	http://data.caf.fr/dataset/c7490d25-8907-4080-b638-d1d43b33e37f/resource/fe4458bd-48b2-4495-b7bc-cddb0d1884fa/download/AAHCom2013.csv
	@wget -O source/AAHCom2014.csv	http://data.caf.fr/dataset/c7490d25-8907-4080-b638-d1d43b33e37f/resource/456530e8-49b3-48ed-803c-25229c614403/download/AAHCom2014.csv
	@wget -O source/AAHCom2015.csv	http://data.caf.fr/dataset/c7490d25-8907-4080-b638-d1d43b33e37f/resource/265c3688-0251-433c-a0db-eea72c95258f/download/AAHCom2015.csv

	# EnfantAgeCom : http://data.caf.fr/dataset/repartition-par-tranche-d-age-des-enfants-couverts-par-des-prestations-caf
	@wget -O source/EnfantAgeCom2009.csv	http://data.caf.fr/dataset/f2efacd4-5276-4cdf-a7a4-5c3e9f7d054c/resource/6a9a4c14-c004-43aa-9c73-46a8bb0328bc/download/enfantageCom2009.csv
	@wget -O source/EnfantAgeCom2010.csv	http://data.caf.fr/dataset/f2efacd4-5276-4cdf-a7a4-5c3e9f7d054c/resource/04ff02f7-cf64-4426-be59-b354c912a46d/download/enfantageCom2010.csv
	@wget -O source/EnfantAgeCom2011.csv	http://data.caf.fr/dataset/f2efacd4-5276-4cdf-a7a4-5c3e9f7d054c/resource/2fa7c247-b555-469f-83f3-3d9474cb32be/download/enfantageCom2011.csv
	@wget -O source/EnfantAgeCom2012.csv	http://data.caf.fr/dataset/f2efacd4-5276-4cdf-a7a4-5c3e9f7d054c/resource/d2e482f6-6b38-4dbe-b3ea-d85203582300/download/enfantageCom2012.csv
	@wget -O source/EnfantAgeCom2013.csv	http://data.caf.fr/dataset/f2efacd4-5276-4cdf-a7a4-5c3e9f7d054c/resource/7e4f551c-64a9-47de-9162-308d2b5f7391/download/enfantageCom2013.csv
	@wget -O source/EnfantAgeCom2014.csv	http://data.caf.fr/dataset/f2efacd4-5276-4cdf-a7a4-5c3e9f7d054c/resource/567d37b3-84de-449b-9089-5ce18bd28160/download/enfantageCom2014.csv
	@wget -O source/EnfantAgeCom2015.csv	http://data.caf.fr/dataset/f2efacd4-5276-4cdf-a7a4-5c3e9f7d054c/resource/5da27638-22e9-49cc-aadc-5db16fdb46ad/download/enfantageCom2015.csv

	# enfantAEEH : http://data.caf.fr/dataset/nombre-d-enfants-couverts-par-l-allocation-d-education-de-l-enfant-handicape-aeeh-par-commune
	@wget -O source/EnfantAEEH2009.csv	http://data.caf.fr/dataset/2c99f216-1474-40b3-a12b-e69afd2f6c4d/resource/bb081154-2e48-4882-85c5-0f465d01479b/download/enfantAEEH2009.csv
	@wget -O source/EnfantAEEH2010.csv	http://data.caf.fr/dataset/2c99f216-1474-40b3-a12b-e69afd2f6c4d/resource/b3e16fc4-77d7-4961-8b4c-c19182ac75fc/download/enfantAEEH2010.csv
	@wget -O source/EnfantAEEH2011.csv	http://data.caf.fr/dataset/2c99f216-1474-40b3-a12b-e69afd2f6c4d/resource/d73969da-1878-4750-8448-15be4e9ce842/download/enfantAEEH2011.csv
	@wget -O source/EnfantAEEH2012.csv	http://data.caf.fr/dataset/2c99f216-1474-40b3-a12b-e69afd2f6c4d/resource/f7543694-3c9e-4971-96ce-a64e3b5ba421/download/enfantAEEH2012.csv
	@wget -O source/EnfantAEEH2013.csv	http://data.caf.fr/dataset/2c99f216-1474-40b3-a12b-e69afd2f6c4d/resource/0160ed9b-fcb7-4acc-a283-655bb11303c3/download/AEEHEnfCom2013.csv
	@wget -O source/EnfantAEEH2014.csv	http://data.caf.fr/dataset/2c99f216-1474-40b3-a12b-e69afd2f6c4d/resource/76738e35-38a1-4a2d-a709-8327ba8f9978/download/enfantAEEH2014.csv
	@wget -O source/EnfantAEEH2015.csv	http://data.caf.fr/dataset/2c99f216-1474-40b3-a12b-e69afd2f6c4d/resource/3f83cade-27c2-45cf-bad6-e557812152ce/download/enfantAEEH2015.csv

	# RSACom : http://data.caf.fr/dataset/foyers-allocataires-percevant-le-revenu-de-solidarite-active-rsa-par-commune
	@wget -O source/RSACom2009.csv	http://data.caf.fr/dataset/b2b4d0bf-faf4-453f-bdb8-66e203b114c8/resource/99ddd753-a3c3-4e8a-8ddf-f58ad778b33a/download/RSACom2009.csv
	@wget -O source/RSACom2010.csv	http://data.caf.fr/dataset/b2b4d0bf-faf4-453f-bdb8-66e203b114c8/resource/cd443296-2f52-4fd9-a40d-b2b6ec3b179e/download/RSACom2010.csv
	@wget -O source/RSACom2011.csv	http://data.caf.fr/dataset/b2b4d0bf-faf4-453f-bdb8-66e203b114c8/resource/1ea185d6-2c00-4ea5-8228-bb25e32dfcca/download/RSACom2011.csv
	@wget -O source/RSACom2012.csv	http://data.caf.fr/dataset/b2b4d0bf-faf4-453f-bdb8-66e203b114c8/resource/23ff16f4-8d89-4012-b50a-ca473edffdab/download/RSACom2012.csv
	@wget -O source/RSACom2013.csv	http://data.caf.fr/dataset/b2b4d0bf-faf4-453f-bdb8-66e203b114c8/resource/f86c1d62-9fae-4cd2-9034-36a4d81f601e/download/RSACom2013.csv
	@wget -O source/RSACom2014.csv	http://data.caf.fr/dataset/b2b4d0bf-faf4-453f-bdb8-66e203b114c8/resource/4c405f7f-a0ac-4d56-b836-c386e38c8c39/download/RSACom2014.csv
	@wget -O source/RSACom2015.csv	http://data.caf.fr/dataset/b2b4d0bf-faf4-453f-bdb8-66e203b114c8/resource/38bb59dd-199a-4f5d-a5b6-012007a03d11/download/RSACom2015.csv

	# EJCom : http://data.caf.fr/dataset/foyers-allocataires-percevant-une-prestation-enfance-et-jeunesse-af-cf-asf-aeeh-et-ars-par-comm
	@wget -O source/EJCom2009.csv	http://data.caf.fr/dataset/a1f4d94f-0df7-42d9-82ee-b8bf18915488/resource/fddf7c97-0d7d-47c2-834a-ae44dfe69d26/download/EJCom2009.csv
	@wget -O source/EJCom2010.csv	http://data.caf.fr/dataset/a1f4d94f-0df7-42d9-82ee-b8bf18915488/resource/b1db157e-db47-4b1b-831b-7e4060300952/download/EJCom2010.csv
	@wget -O source/EJCom2011.csv	http://data.caf.fr/dataset/a1f4d94f-0df7-42d9-82ee-b8bf18915488/resource/c1a2f684-b7e4-4b92-9ac9-8bbcbcb35468/download/EJCom2011.csv
	@wget -O source/EJCom2012.csv	http://data.caf.fr/dataset/a1f4d94f-0df7-42d9-82ee-b8bf18915488/resource/d67fa36f-5f87-40ac-8518-b62566ce1be2/download/EJCom2012.csv
	@wget -O source/EJCom2013.csv	http://data.caf.fr/dataset/a1f4d94f-0df7-42d9-82ee-b8bf18915488/resource/9d1a5311-c886-4dee-8ebf-626059a474b2/download/EJCom2013.csv
	@wget -O source/EJCom2014.csv	http://data.caf.fr/dataset/a1f4d94f-0df7-42d9-82ee-b8bf18915488/resource/1fc10e2d-781e-422e-a0b0-58b51e9bbb8f/download/EJCom2014.csv
	@wget -O source/EJCom2015.csv	http://data.caf.fr/dataset/a1f4d94f-0df7-42d9-82ee-b8bf18915488/resource/ed83b335-fc5a-472c-b430-2504068e224b/download/EJCom2015.csv

	# LogPersPrestaCom : http://data.caf.fr/dataset/population-des-foyers-allocatair
	@wget -O source/LOGPersPrestaCom2009.csv	http://data.caf.fr/dataset/ad042a79-c4b8-4f80-88ef-7d410e121404/resource/18e53a92-da86-4c9d-9488-25c0c6229538/download/LOGPersPrestaCom2009.csv
	@wget -O source/LOGPersPrestaCom2010.csv	http://data.caf.fr/dataset/ad042a79-c4b8-4f80-88ef-7d410e121404/resource/b2f4a665-2dcc-4eae-b777-d90563641aad/download/LOGPersPrestaCom2010.csv
	@wget -O source/LOGPersPrestaCom2011.csv	http://data.caf.fr/dataset/ad042a79-c4b8-4f80-88ef-7d410e121404/resource/b324da48-dc27-4611-ac23-3eff6c1febff/download/LOGPersPrestaCom2011.csv
	@wget -O source/LOGPersPrestaCom2012.csv	http://data.caf.fr/dataset/ad042a79-c4b8-4f80-88ef-7d410e121404/resource/03f7ea8c-53e4-4c92-8a21-03863d61373b/download/LOGPersPrestaCom2012.csv
	@wget -O source/LOGPersPrestaCom2013.csv	http://data.caf.fr/dataset/ad042a79-c4b8-4f80-88ef-7d410e121404/resource/48c22f83-2dcc-4b20-a8c8-ba073ef890cf/download/LOGPersPrestaCom2013.csv
	@wget -O source/LOGPersPrestaCom2014.csv	http://data.caf.fr/dataset/ad042a79-c4b8-4f80-88ef-7d410e121404/resource/2447b641-d819-449a-9285-454e25664f46/download/LOGPersPrestaCom2014.csv
	@wget -O source/LOGPersPrestaCom2015.csv	http://data.caf.fr/dataset/ad042a79-c4b8-4f80-88ef-7d410e121404/resource/afe7c84b-2ea9-4016-8a56-5a4142bc039e/download/LOGPersPrestaCom2015.csv

	# EnfantARS : http://data.caf.fr/dataset/nombre-denfants-couverts-par-l-allocation-de-rentree-scolaire-ars-par-commune
	@wget -O source/EnfantARS2009.csv	http://data.caf.fr/dataset/4ddb8c82-5a43-48d3-9b2b-40512e807087/resource/a7790e86-f5ab-471e-b427-c8507d728550/download/enfantARS2009.csv
	@wget -O source/EnfantARS2010.csv	http://data.caf.fr/dataset/4ddb8c82-5a43-48d3-9b2b-40512e807087/resource/02adcd2b-ffb3-4537-89c2-38723486c688/download/enfantARS2010.csv
	@wget -O source/EnfantARS2011.csv	http://data.caf.fr/dataset/4ddb8c82-5a43-48d3-9b2b-40512e807087/resource/d6d2e400-d511-471e-8d4e-70250bf68043/download/enfantARS2011.csv
	@wget -O source/EnfantARS2012.csv	http://data.caf.fr/dataset/4ddb8c82-5a43-48d3-9b2b-40512e807087/resource/54562221-7223-4554-a29f-aae23b370590/download/enfantARS2012.csv
	@wget -O source/EnfantARS2013.csv	http://data.caf.fr/dataset/4ddb8c82-5a43-48d3-9b2b-40512e807087/resource/198a5723-32fa-4fb7-903e-15076badf0e0/download/enfantARS2013.csv
	@wget -O source/EnfantARS2014.csv	http://data.caf.fr/dataset/4ddb8c82-5a43-48d3-9b2b-40512e807087/resource/bd67d932-1987-4a90-a563-ccce15346ed3/download/enfantARS2014.csv
	@wget -O source/EnfantARS2015.csv	http://data.caf.fr/dataset/4ddb8c82-5a43-48d3-9b2b-40512e807087/resource/9171579b-9b2e-4a27-b0e7-188763ad4453/download/enfantARS2015.csv



data_commune:
	python scripts/DependancePrestaCom.py
	python scripts/BasrevnuCom.py
	python scripts/NivComTotal.py
	python scripts/ConfigFamiliale.py
	python scripts/TrancheAge.py
	python scripts/LogCom.py
	python scripts/PajeCom.py
	python scripts/RsaPersCom.py
	python scripts/AAHCom.py
	python scripts/EnfantAgeCom.py
	python scripts/EnfantAEEH.py
	python scripts/RSACom.py
	python scripts/EJCom.py
	python scripts/LogPersPrestaCom.py
	python scripts/EnfantARS.py

merging:
	@wget -O source/commune_insee.csv  "http://public.opendatasoft.com/explore/dataset/correspondance-code-insee-code-postal/download/?format=csv&timezone=Europe/Berlin&use_labels_for_header=true"
	python scripts/Merging.py
