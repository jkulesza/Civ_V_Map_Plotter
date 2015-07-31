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

t1 :
	$(eval SIZE := duel)
	$(eval TEST := test_0001)
	@echo "+-------------------------------------------------------------------------------"
	@echo "| Running $(TEST)"
	@echo "+-------------------------------------------------------------------------------"
	@cd $(TEST); ln -sf $(PATH_TO_PY_FILES)/*py .
	cd $(TEST); $(PY_EXE) $(PRODUCT) map.png         $(SIZE) --diagnostic                --verbose 1
	cd $(TEST); $(PY_EXE) $(PRODUCT) map_cropped.png $(SIZE) --nocrop                    --verbose 1 
	cd $(TEST); $(PY_EXE) $(PRODUCT) map_cropped.png $(SIZE) --nocrop --diagnostic --pdf --verbose 1 
	cd $(TEST); $(PY_EXE) $(PRODUCT) map_cropped.png $(SIZE) --nocrop --pdf              --verbose 1 
	cd $(TEST); convert -density 200 -resize 50% map_cropped_processed.pdf pdf_converted_to.png

t2 :
	$(eval SIZE := tiny)
	$(eval TEST := test_0002)
	@echo "+-------------------------------------------------------------------------------"
	@echo "| Running $(TEST)"
	@echo "+-------------------------------------------------------------------------------"
	@cd $(TEST); ln -sf $(PATH_TO_PY_FILES)/*py .
	cd $(TEST); $(PY_EXE) $(PRODUCT) map.png         $(SIZE) --diagnostic                --verbose 1  
	cd $(TEST); $(PY_EXE) $(PRODUCT) map_cropped.png $(SIZE) --nocrop                    --verbose 1  
	cd $(TEST); $(PY_EXE) $(PRODUCT) map_cropped.png $(SIZE) --nocrop --diagnostic --pdf --verbose 1  
	cd $(TEST); $(PY_EXE) $(PRODUCT) map_cropped.png $(SIZE) --nocrop --pdf              --verbose 1  
	cd $(TEST); convert -density 200 -resize 50% map_cropped_processed.pdf pdf_converted_to.png
 
t3 :
	$(eval SIZE := small)
	$(eval TEST := test_0003)
	@echo "+-------------------------------------------------------------------------------"
	@echo "| Running $(TEST)"
	@echo "+-------------------------------------------------------------------------------"
	@cd $(TEST); ln -sf $(PATH_TO_PY_FILES)/*py .
	cd $(TEST); $(PY_EXE) $(PRODUCT) map.png         $(SIZE) --diagnostic                --verbose 1  
	cd $(TEST); $(PY_EXE) $(PRODUCT) map_cropped.png $(SIZE) --nocrop                    --verbose 1  
	cd $(TEST); $(PY_EXE) $(PRODUCT) map_cropped.png $(SIZE) --nocrop --diagnostic --pdf --verbose 1  
	cd $(TEST); $(PY_EXE) $(PRODUCT) map_cropped.png $(SIZE) --nocrop --pdf              --verbose 1  
	cd $(TEST); convert -density 200 -resize 50% map_cropped_processed.pdf pdf_converted_to.png
 
t4 :
	$(eval SIZE := standard)
	$(eval TEST := test_0004)
	@echo "+-------------------------------------------------------------------------------"
	@echo "| Running $(TEST)"
	@echo "+-------------------------------------------------------------------------------"
	@cd $(TEST); ln -sf $(PATH_TO_PY_FILES)/*py .
	cd $(TEST); $(PY_EXE) $(PRODUCT) map.png         $(SIZE) --diagnostic                --verbose 1  
	cd $(TEST); $(PY_EXE) $(PRODUCT) map_cropped.png $(SIZE) --nocrop                    --verbose 1  
	cd $(TEST); $(PY_EXE) $(PRODUCT) map_cropped.png $(SIZE) --nocrop --diagnostic --pdf --verbose 1  
	cd $(TEST); $(PY_EXE) $(PRODUCT) map_cropped.png $(SIZE) --nocrop --pdf              --verbose 1  
	cd $(TEST); convert -density 200 -resize 50% map_cropped_processed.pdf pdf_converted_to.png
 
t5 :
	$(eval SIZE := large)
	$(eval TEST := test_0005)
	@echo "+-------------------------------------------------------------------------------"
	@echo "| Running $(TEST)"
	@echo "+-------------------------------------------------------------------------------"
	@cd $(TEST); ln -sf $(PATH_TO_PY_FILES)/*py .
	cd $(TEST); $(PY_EXE) $(PRODUCT) map.png         $(SIZE) --diagnostic                --verbose 1  
	cd $(TEST); $(PY_EXE) $(PRODUCT) map_cropped.png $(SIZE) --nocrop                    --verbose 1  
	cd $(TEST); $(PY_EXE) $(PRODUCT) map_cropped.png $(SIZE) --nocrop --diagnostic --pdf --verbose 1  
	cd $(TEST); $(PY_EXE) $(PRODUCT) map_cropped.png $(SIZE) --nocrop --pdf              --verbose 1  
	cd $(TEST); convert -density 200 -resize 50% map_cropped_processed.pdf pdf_converted_to.png
 
t6 :
	$(eval SIZE := huge)
	$(eval TEST := test_0006)
	@echo "+-------------------------------------------------------------------------------"
	@echo "| Running $(TEST)"
	@echo "+-------------------------------------------------------------------------------"
	@cd $(TEST); ln -sf $(PATH_TO_PY_FILES)/*py .
	cd $(TEST); $(PY_EXE) $(PRODUCT) map.png         $(SIZE) --diagnostic                --verbose 1  
	cd $(TEST); $(PY_EXE) $(PRODUCT) map_cropped.png $(SIZE) --nocrop                    --verbose 1  
	cd $(TEST); $(PY_EXE) $(PRODUCT) map_cropped.png $(SIZE) --nocrop --diagnostic --pdf --verbose 1  
	cd $(TEST); $(PY_EXE) $(PRODUCT) map_cropped.png $(SIZE) --nocrop --pdf              --verbose 1  
	cd $(TEST); convert -density 200 -resize 50% map_cropped_processed.pdf pdf_converted_to.png
 
test : t1 t2 t3 t4 t5 t6

all : test

clean :
	rm -rf test_*/*py
	rm -rf test_*/*dat
	rm -rf test_*/*cropped*png
	rm -rf test_*/*cropped*pdf

