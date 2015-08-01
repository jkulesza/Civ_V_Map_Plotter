PATH_TO_PY_FILES = ../..
PRODUCT = Civ_V_Map_Plotter.py
PY_EXE = /sw/bin/python2.7

default :
	@echo ""
	@echo "Select 'make' target:"
	@echo "   - tN with N = 1 ... Number of Test Cases."
	@echo "   - test (to run all test cases)."
	@echo "   - clean (to remove all test-case generated files."
	@echo ""

# Diagnostic PNG tests.

t1 :
	$(eval SIZE := duel)
	$(eval DIR := 01_SC3)
	@echo "+-------------------------------------------------------------------------------"
	@echo "| Running $@"
	@echo "+-------------------------------------------------------------------------------"
	@cd $(DIR); ln -sf $(PATH_TO_PY_FILES)/*py .
	cd $(DIR); $(PY_EXE) $(PRODUCT) map.png $(SIZE) --diagnostic --verbosity 1 --method sc3

t2 :
	$(eval SIZE := tiny)
	$(eval DIR := 02_SC3)
	@echo "+-------------------------------------------------------------------------------"
	@echo "| Running $@"
	@echo "+-------------------------------------------------------------------------------"
	@cd $(DIR); ln -sf $(PATH_TO_PY_FILES)/*py .
	cd $(DIR); $(PY_EXE) $(PRODUCT) map.png $(SIZE) --diagnostic --verbosity 1 --method sc3

t3 :
	$(eval SIZE := small)
	$(eval DIR := 03_SC3)
	@echo "+-------------------------------------------------------------------------------"
	@echo "| Running $@"
	@echo "+-------------------------------------------------------------------------------"
	@cd $(DIR); ln -sf $(PATH_TO_PY_FILES)/*py .
	cd $(DIR); $(PY_EXE) $(PRODUCT) map.png $(SIZE) --diagnostic --verbosity 1 --method sc3

t4 :
	$(eval SIZE := standard)
	$(eval DIR := 04_SC3)
	@echo "+-------------------------------------------------------------------------------"
	@echo "| Running $@"
	@echo "+-------------------------------------------------------------------------------"
	@cd $(DIR); ln -sf $(PATH_TO_PY_FILES)/*py .
	cd $(DIR); $(PY_EXE) $(PRODUCT) map.png $(SIZE) --diagnostic --verbosity 1 --method sc3

t5 :
	$(eval SIZE := large)
	$(eval DIR := 05_SC3)
	@echo "+-------------------------------------------------------------------------------"
	@echo "| Running $@"
	@echo "+-------------------------------------------------------------------------------"
	@cd $(DIR); ln -sf $(PATH_TO_PY_FILES)/*py .
	cd $(DIR); $(PY_EXE) $(PRODUCT) map.png $(SIZE) --diagnostic --verbosity 1 --method sc3

t6 :
	$(eval SIZE := huge)
	$(eval DIR := 06_SC3)
	@echo "+-------------------------------------------------------------------------------"
	@echo "| Running $@"
	@echo "+-------------------------------------------------------------------------------"
	@cd $(DIR); ln -sf $(PATH_TO_PY_FILES)/*py .
	cd $(DIR); $(PY_EXE) $(PRODUCT) map.png $(SIZE) --diagnostic --verbosity 1 --method sc3

t7 :
	$(eval SIZE := duel)
	$(eval DIR := 07_SC4SB)
	@echo "+-------------------------------------------------------------------------------"
	@echo "| Running $@"
	@echo "+-------------------------------------------------------------------------------"
	@cd $(DIR); ln -sf $(PATH_TO_PY_FILES)/*py .
	cd $(DIR); $(PY_EXE) $(PRODUCT) map.png $(SIZE) --diagnostic --verbosity 1 --method sc4sb

t8 :
	$(eval SIZE := tiny)
	$(eval DIR := 08_SC4SB)
	@echo "+-------------------------------------------------------------------------------"
	@echo "| Running $@"
	@echo "+-------------------------------------------------------------------------------"
	@cd $(DIR); ln -sf $(PATH_TO_PY_FILES)/*py .
	cd $(DIR); $(PY_EXE) $(PRODUCT) map.png $(SIZE) --diagnostic --verbosity 1 --method sc4sb

t9 :
	$(eval SIZE := small)
	$(eval DIR := 09_SC4SB)
	@echo "+-------------------------------------------------------------------------------"
	@echo "| Running $@"
	@echo "+-------------------------------------------------------------------------------"
	@cd $(DIR); ln -sf $(PATH_TO_PY_FILES)/*py .
	cd $(DIR); $(PY_EXE) $(PRODUCT) map.png $(SIZE) --diagnostic --verbosity 1 --method sc4sb

t10 :
	$(eval SIZE := standard)
	$(eval DIR := 10_SC4SB)
	@echo "+-------------------------------------------------------------------------------"
	@echo "| Running $@"
	@echo "+-------------------------------------------------------------------------------"
	@cd $(DIR); ln -sf $(PATH_TO_PY_FILES)/*py .
	cd $(DIR); $(PY_EXE) $(PRODUCT) map.png $(SIZE) --diagnostic --verbosity 1 --method sc4sb

t11 :
	$(eval SIZE := large)
	$(eval DIR := 11_SC4SB)
	@echo "+-------------------------------------------------------------------------------"
	@echo "| Running $@"
	@echo "+-------------------------------------------------------------------------------"
	@cd $(DIR); ln -sf $(PATH_TO_PY_FILES)/*py .
	cd $(DIR); $(PY_EXE) $(PRODUCT) map.png $(SIZE) --diagnostic --verbosity 1 --method sc4sb

t12 :
	$(eval SIZE := huge)
	$(eval DIR := 12_SC4SB)
	@echo "+-------------------------------------------------------------------------------"
	@echo "| Running $@"
	@echo "+-------------------------------------------------------------------------------"
	@cd $(DIR); ln -sf $(PATH_TO_PY_FILES)/*py .
	cd $(DIR); $(PY_EXE) $(PRODUCT) map.png $(SIZE) --diagnostic --verbosity 1 --method sc4sb

# PNG tests.

t13 :
	$(eval SIZE := duel)
	$(eval DIR := 01_SC3)
	@echo "+-------------------------------------------------------------------------------"
	@echo "| Running $@"
	@echo "+-------------------------------------------------------------------------------"
	@cd $(DIR); ln -sf $(PATH_TO_PY_FILES)/*py .
	cd $(DIR); $(PY_EXE) $(PRODUCT) map.png $(SIZE) --verbosity 1 --method sc3

t14 :
	$(eval SIZE := tiny)
	$(eval DIR := 02_SC3)
	@echo "+-------------------------------------------------------------------------------"
	@echo "| Running $@"
	@echo "+-------------------------------------------------------------------------------"
	@cd $(DIR); ln -sf $(PATH_TO_PY_FILES)/*py .
	cd $(DIR); $(PY_EXE) $(PRODUCT) map.png $(SIZE) --verbosity 1 --method sc3

t15 :
	$(eval SIZE := small)
	$(eval DIR := 03_SC3)
	@echo "+-------------------------------------------------------------------------------"
	@echo "| Running $@"
	@echo "+-------------------------------------------------------------------------------"
	@cd $(DIR); ln -sf $(PATH_TO_PY_FILES)/*py .
	cd $(DIR); $(PY_EXE) $(PRODUCT) map.png $(SIZE) --verbosity 1 --method sc3

t16 :
	$(eval SIZE := standard)
	$(eval DIR := 04_SC3)
	@echo "+-------------------------------------------------------------------------------"
	@echo "| Running $@"
	@echo "+-------------------------------------------------------------------------------"
	@cd $(DIR); ln -sf $(PATH_TO_PY_FILES)/*py .
	cd $(DIR); $(PY_EXE) $(PRODUCT) map.png $(SIZE) --verbosity 1 --method sc3

t17 :
	$(eval SIZE := large)
	$(eval DIR := 05_SC3)
	@echo "+-------------------------------------------------------------------------------"
	@echo "| Running $@"
	@echo "+-------------------------------------------------------------------------------"
	@cd $(DIR); ln -sf $(PATH_TO_PY_FILES)/*py .
	cd $(DIR); $(PY_EXE) $(PRODUCT) map.png $(SIZE) --verbosity 1 --method sc3

t18 :
	$(eval SIZE := huge)
	$(eval DIR := 06_SC3)
	@echo "+-------------------------------------------------------------------------------"
	@echo "| Running $@"
	@echo "+-------------------------------------------------------------------------------"
	@cd $(DIR); ln -sf $(PATH_TO_PY_FILES)/*py .
	cd $(DIR); $(PY_EXE) $(PRODUCT) map.png $(SIZE) --verbosity 1 --method sc3

t19 :
	$(eval SIZE := duel)
	$(eval DIR := 07_SC4SB)
	@echo "+-------------------------------------------------------------------------------"
	@echo "| Running $@"
	@echo "+-------------------------------------------------------------------------------"
	@cd $(DIR); ln -sf $(PATH_TO_PY_FILES)/*py .
	cd $(DIR); $(PY_EXE) $(PRODUCT) map.png $(SIZE) --verbosity 1 --method sc4sb

t20 :
	$(eval SIZE := tiny)
	$(eval DIR := 08_SC4SB)
	@echo "+-------------------------------------------------------------------------------"
	@echo "| Running $@"
	@echo "+-------------------------------------------------------------------------------"
	@cd $(DIR); ln -sf $(PATH_TO_PY_FILES)/*py .
	cd $(DIR); $(PY_EXE) $(PRODUCT) map.png $(SIZE) --verbosity 1 --method sc4sb

t21 :
	$(eval SIZE := small)
	$(eval DIR := 09_SC4SB)
	@echo "+-------------------------------------------------------------------------------"
	@echo "| Running $@"
	@echo "+-------------------------------------------------------------------------------"
	@cd $(DIR); ln -sf $(PATH_TO_PY_FILES)/*py .
	cd $(DIR); $(PY_EXE) $(PRODUCT) map.png $(SIZE) --verbosity 1 --method sc4sb

t22 :
	$(eval SIZE := standard)
	$(eval DIR := 10_SC4SB)
	@echo "+-------------------------------------------------------------------------------"
	@echo "| Running $@"
	@echo "+-------------------------------------------------------------------------------"
	@cd $(DIR); ln -sf $(PATH_TO_PY_FILES)/*py .
	cd $(DIR); $(PY_EXE) $(PRODUCT) map.png $(SIZE) --verbosity 1 --method sc4sb

t23 :
	$(eval SIZE := large)
	$(eval DIR := 11_SC4SB)
	@echo "+-------------------------------------------------------------------------------"
	@echo "| Running $@"
	@echo "+-------------------------------------------------------------------------------"
	@cd $(DIR); ln -sf $(PATH_TO_PY_FILES)/*py .
	cd $(DIR); $(PY_EXE) $(PRODUCT) map.png $(SIZE) --verbosity 1 --method sc4sb

t24 :
	$(eval SIZE := huge)
	$(eval DIR := 12_SC4SB)
	@echo "+-------------------------------------------------------------------------------"
	@echo "| Running $@"
	@echo "+-------------------------------------------------------------------------------"
	@cd $(DIR); ln -sf $(PATH_TO_PY_FILES)/*py .
	cd $(DIR); $(PY_EXE) $(PRODUCT) map.png $(SIZE) --verbosity 1 --method sc4sb

# Diagnostic PDF tests.

t25 :
	$(eval SIZE := duel)
	$(eval DIR := 01_SC3)
	@echo "+-------------------------------------------------------------------------------"
	@echo "| Running $@"
	@echo "+-------------------------------------------------------------------------------"
	@cd $(DIR); ln -sf $(PATH_TO_PY_FILES)/*py .
	cd $(DIR); $(PY_EXE) $(PRODUCT) map.png $(SIZE) --diagnostic --pdf --verbosity 1 --method sc3

t26 :
	$(eval SIZE := tiny)
	$(eval DIR := 02_SC3)
	@echo "+-------------------------------------------------------------------------------"
	@echo "| Running $@"
	@echo "+-------------------------------------------------------------------------------"
	@cd $(DIR); ln -sf $(PATH_TO_PY_FILES)/*py .
	cd $(DIR); $(PY_EXE) $(PRODUCT) map.png $(SIZE) --diagnostic --pdf --verbosity 1 --method sc3

t27 :
	$(eval SIZE := small)
	$(eval DIR := 03_SC3)
	@echo "+-------------------------------------------------------------------------------"
	@echo "| Running $@"
	@echo "+-------------------------------------------------------------------------------"
	@cd $(DIR); ln -sf $(PATH_TO_PY_FILES)/*py .
	cd $(DIR); $(PY_EXE) $(PRODUCT) map.png $(SIZE) --diagnostic --pdf --verbosity 1 --method sc3

t28 :
	$(eval SIZE := standard)
	$(eval DIR := 04_SC3)
	@echo "+-------------------------------------------------------------------------------"
	@echo "| Running $@"
	@echo "+-------------------------------------------------------------------------------"
	@cd $(DIR); ln -sf $(PATH_TO_PY_FILES)/*py .
	cd $(DIR); $(PY_EXE) $(PRODUCT) map.png $(SIZE) --diagnostic --pdf --verbosity 1 --method sc3

t29 :
	$(eval SIZE := large)
	$(eval DIR := 05_SC3)
	@echo "+-------------------------------------------------------------------------------"
	@echo "| Running $@"
	@echo "+-------------------------------------------------------------------------------"
	@cd $(DIR); ln -sf $(PATH_TO_PY_FILES)/*py .
	cd $(DIR); $(PY_EXE) $(PRODUCT) map.png $(SIZE) --diagnostic --pdf --verbosity 1 --method sc3

t30 :
	$(eval SIZE := huge)
	$(eval DIR := 06_SC3)
	@echo "+-------------------------------------------------------------------------------"
	@echo "| Running $@"
	@echo "+-------------------------------------------------------------------------------"
	@cd $(DIR); ln -sf $(PATH_TO_PY_FILES)/*py .
	cd $(DIR); $(PY_EXE) $(PRODUCT) map.png $(SIZE) --diagnostic --pdf --verbosity 1 --method sc3

t31 :
	$(eval SIZE := duel)
	$(eval DIR := 07_SC4SB)
	@echo "+-------------------------------------------------------------------------------"
	@echo "| Running $@"
	@echo "+-------------------------------------------------------------------------------"
	@cd $(DIR); ln -sf $(PATH_TO_PY_FILES)/*py .
	cd $(DIR); $(PY_EXE) $(PRODUCT) map.png $(SIZE) --diagnostic --pdf --verbosity 1 --method sc4sb

t32 :
	$(eval SIZE := tiny)
	$(eval DIR := 08_SC4SB)
	@echo "+-------------------------------------------------------------------------------"
	@echo "| Running $@"
	@echo "+-------------------------------------------------------------------------------"
	@cd $(DIR); ln -sf $(PATH_TO_PY_FILES)/*py .
	cd $(DIR); $(PY_EXE) $(PRODUCT) map.png $(SIZE) --diagnostic --pdf --verbosity 1 --method sc4sb

t33 :
	$(eval SIZE := small)
	$(eval DIR := 09_SC4SB)
	@echo "+-------------------------------------------------------------------------------"
	@echo "| Running $@"
	@echo "+-------------------------------------------------------------------------------"
	@cd $(DIR); ln -sf $(PATH_TO_PY_FILES)/*py .
	cd $(DIR); $(PY_EXE) $(PRODUCT) map.png $(SIZE) --diagnostic --pdf --verbosity 1 --method sc4sb

t34 :
	$(eval SIZE := standard)
	$(eval DIR := 10_SC4SB)
	@echo "+-------------------------------------------------------------------------------"
	@echo "| Running $@"
	@echo "+-------------------------------------------------------------------------------"
	@cd $(DIR); ln -sf $(PATH_TO_PY_FILES)/*py .
	cd $(DIR); $(PY_EXE) $(PRODUCT) map.png $(SIZE) --diagnostic --pdf --verbosity 1 --method sc4sb

t35 :
	$(eval SIZE := large)
	$(eval DIR := 11_SC4SB)
	@echo "+-------------------------------------------------------------------------------"
	@echo "| Running $@"
	@echo "+-------------------------------------------------------------------------------"
	@cd $(DIR); ln -sf $(PATH_TO_PY_FILES)/*py .
	cd $(DIR); $(PY_EXE) $(PRODUCT) map.png $(SIZE) --diagnostic --pdf --verbosity 1 --method sc4sb

t36 :
	$(eval SIZE := huge)
	$(eval DIR := 12_SC4SB)
	@echo "+-------------------------------------------------------------------------------"
	@echo "| Running $@"
	@echo "+-------------------------------------------------------------------------------"
	@cd $(DIR); ln -sf $(PATH_TO_PY_FILES)/*py .
	cd $(DIR); $(PY_EXE) $(PRODUCT) map.png $(SIZE) --diagnostic --pdf --verbosity 1 --method sc4sb

# PDF tests.

t37 :
	$(eval SIZE := duel)
	$(eval DIR := 01_SC3)
	@echo "+-------------------------------------------------------------------------------"
	@echo "| Running $@"
	@echo "+-------------------------------------------------------------------------------"
	@cd $(DIR); ln -sf $(PATH_TO_PY_FILES)/*py .
	cd $(DIR); $(PY_EXE) $(PRODUCT) map.png $(SIZE) --pdf --verbosity 1 --method sc3
	cd $(DIR); convert -density 200 -resize 50% map_cropped_processed.pdf map_pdf_converted_to.png

t38 :
	$(eval SIZE := tiny)
	$(eval DIR := 02_SC3)
	@echo "+-------------------------------------------------------------------------------"
	@echo "| Running $@"
	@echo "+-------------------------------------------------------------------------------"
	@cd $(DIR); ln -sf $(PATH_TO_PY_FILES)/*py .
	cd $(DIR); $(PY_EXE) $(PRODUCT) map.png $(SIZE) --pdf --verbosity 1 --method sc3
	cd $(DIR); convert -density 200 -resize 50% map_cropped_processed.pdf map_pdf_converted_to.png

t39 :
	$(eval SIZE := small)
	$(eval DIR := 03_SC3)
	@echo "+-------------------------------------------------------------------------------"
	@echo "| Running $@"
	@echo "+-------------------------------------------------------------------------------"
	@cd $(DIR); ln -sf $(PATH_TO_PY_FILES)/*py .
	cd $(DIR); $(PY_EXE) $(PRODUCT) map.png $(SIZE) --pdf --verbosity 1 --method sc3
	cd $(DIR); convert -density 200 -resize 50% map_cropped_processed.pdf map_pdf_converted_to.png

t40 :
	$(eval SIZE := standard)
	$(eval DIR := 04_SC3)
	@echo "+-------------------------------------------------------------------------------"
	@echo "| Running $@"
	@echo "+-------------------------------------------------------------------------------"
	@cd $(DIR); ln -sf $(PATH_TO_PY_FILES)/*py .
	cd $(DIR); $(PY_EXE) $(PRODUCT) map.png $(SIZE) --pdf --verbosity 1 --method sc3
	cd $(DIR); convert -density 200 -resize 50% map_cropped_processed.pdf map_pdf_converted_to.png

t41 :
	$(eval SIZE := large)
	$(eval DIR := 05_SC3)
	@echo "+-------------------------------------------------------------------------------"
	@echo "| Running $@"
	@echo "+-------------------------------------------------------------------------------"
	@cd $(DIR); ln -sf $(PATH_TO_PY_FILES)/*py .
	cd $(DIR); $(PY_EXE) $(PRODUCT) map.png $(SIZE) --pdf --verbosity 1 --method sc3
	cd $(DIR); convert -density 200 -resize 50% map_cropped_processed.pdf map_pdf_converted_to.png

t42 :
	$(eval SIZE := huge)
	$(eval DIR := 06_SC3)
	@echo "+-------------------------------------------------------------------------------"
	@echo "| Running $@"
	@echo "+-------------------------------------------------------------------------------"
	@cd $(DIR); ln -sf $(PATH_TO_PY_FILES)/*py .
	cd $(DIR); $(PY_EXE) $(PRODUCT) map.png $(SIZE) --pdf --verbosity 1 --method sc3
	cd $(DIR); convert -density 200 -resize 50% map_cropped_processed.pdf map_pdf_converted_to.png

t43 :
	$(eval SIZE := duel)
	$(eval DIR := 07_SC4SB)
	@echo "+-------------------------------------------------------------------------------"
	@echo "| Running $@"
	@echo "+-------------------------------------------------------------------------------"
	@cd $(DIR); ln -sf $(PATH_TO_PY_FILES)/*py .
	cd $(DIR); $(PY_EXE) $(PRODUCT) map.png $(SIZE) --pdf --verbosity 1 --method sc4sb
	cd $(DIR); convert -density 200 -resize 50% map_cropped_processed.pdf map_pdf_converted_to.png

t44 :
	$(eval SIZE := tiny)
	$(eval DIR := 08_SC4SB)
	@echo "+-------------------------------------------------------------------------------"
	@echo "| Running $@"
	@echo "+-------------------------------------------------------------------------------"
	@cd $(DIR); ln -sf $(PATH_TO_PY_FILES)/*py .
	cd $(DIR); $(PY_EXE) $(PRODUCT) map.png $(SIZE) --pdf --verbosity 1 --method sc4sb
	cd $(DIR); convert -density 200 -resize 50% map_cropped_processed.pdf map_pdf_converted_to.png

t45 :
	$(eval SIZE := small)
	$(eval DIR := 09_SC4SB)
	@echo "+-------------------------------------------------------------------------------"
	@echo "| Running $@"
	@echo "+-------------------------------------------------------------------------------"
	@cd $(DIR); ln -sf $(PATH_TO_PY_FILES)/*py .
	cd $(DIR); $(PY_EXE) $(PRODUCT) map.png $(SIZE) --pdf --verbosity 1 --method sc4sb
	cd $(DIR); convert -density 200 -resize 50% map_cropped_processed.pdf map_pdf_converted_to.png

t46 :
	$(eval SIZE := standard)
	$(eval DIR := 10_SC4SB)
	@echo "+-------------------------------------------------------------------------------"
	@echo "| Running $@"
	@echo "+-------------------------------------------------------------------------------"
	@cd $(DIR); ln -sf $(PATH_TO_PY_FILES)/*py .
	cd $(DIR); $(PY_EXE) $(PRODUCT) map.png $(SIZE) --pdf --verbosity 1 --method sc4sb
	cd $(DIR); convert -density 200 -resize 50% map_cropped_processed.pdf map_pdf_converted_to.png

t47 :
	$(eval SIZE := large)
	$(eval DIR := 11_SC4SB)
	@echo "+-------------------------------------------------------------------------------"
	@echo "| Running $@"
	@echo "+-------------------------------------------------------------------------------"
	@cd $(DIR); ln -sf $(PATH_TO_PY_FILES)/*py .
	cd $(DIR); $(PY_EXE) $(PRODUCT) map.png $(SIZE) --pdf --verbosity 1 --method sc4sb
	cd $(DIR); convert -density 200 -resize 50% map_cropped_processed.pdf map_pdf_converted_to.png

t48 :
	$(eval SIZE := huge)
	$(eval DIR := 12_SC4SB)
	@echo "+-------------------------------------------------------------------------------"
	@echo "| Running $@"
	@echo "+-------------------------------------------------------------------------------"
	@cd $(DIR); ln -sf $(PATH_TO_PY_FILES)/*py .
	cd $(DIR); $(PY_EXE) $(PRODUCT) map.png $(SIZE) --pdf --verbosity 1 --method sc4sb
	cd $(DIR); convert -density 200 -resize 50% map_cropped_processed.pdf map_pdf_converted_to.png

diagnostic_png: t1  t2  t3  t4  t5  t6  t7  t8  t9  t10 t11 t12
png           : t13 t14 t15 t16 t17 t18 t19 t20 t21 t22 t23 t24
diagnostic_pdf: t25 t26 t27 t28 t29 t30 t31 t32 t33 t34 t35 t36
pdf           : t37 t38 t39 t40 t41 t42 t43 t44 t45 t46 t47 t48

all : diagnostic_png png diagnostic_pdf pdf

clean :
	rm -rf */*py
	rm -rf */*dat
	rm -rf */*cropped*png
	rm -rf */*cropped*pdf
	rm -rf */*converted*png

