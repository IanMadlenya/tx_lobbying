wget=\wget --quiet --no-check-certificate

help:
	@echo "help:"
	@echo "  help          : this help"
	@echo "  lobcon        : download lobbyist registrations"
	@echo "  expenses      : download lobbyist expenses"
	@echo "  nomenklatura  : download interest canonical names"
	@echo "  all           : download everything"


# Download links found on: http://www.ethics.state.tx.us/dfs/loblists.htm
.PHONY: lobcon
lobcon:
	mkdir -p $@
	rm -rf $@/*.xls
	cd $@ && $(wget) --quiet http://www.ethics.state.tx.us/tedd/LobCon15.xls
	cd $@ && $(wget) --quiet http://www.ethics.state.tx.us/tedd/LobCon14.xls
	cd $@ && $(wget) --quiet http://www.ethics.state.tx.us/tedd/LobCon13.xls
	cd $@ && $(wget) --quiet http://www.ethics.state.tx.us/tedd/LobCon12.xls
	cd $@ && $(wget) --quiet http://www.ethics.state.tx.us/tedd/LobCon11.xls
	cd $@ && $(wget) --quiet http://www.ethics.state.tx.us/tedd/LobCon10.xls
	cd $@ && $(wget) --quiet http://www.ethics.state.tx.us/tedd/LobCon09.xls


# convert the xls to csv so the scraper can read them
lobcon/csv:
	@echo "Converting Lobbyist Registrations from XLS to CSV"
	$(foreach file, $(wildcard lobcon/*.xls), \
		in2csv $(file) > $(subst xls,csv,$(file));)


expenses:
	mkdir -p $@
	$(wget) --quiet http://www.ethics.state.tx.us/tedd/TEC_LA_CSV.zip
	unzip -o -u TEC_LA_CSV.zip -d $@
	rm TEC_LA_CSV.zip


# CSV of mappings of canonical Interest names
nomenklatura:
	mkdir -p nomenklatura
	curl --silent "http://opennames.org/api/2/entities?dataset=tx-lobbying-interests&format=csv" | \
	  csvsort --reverse -c 4 > $@/interests.csv
	curl --silent "http://opennames.org/api/2/entities?dataset=tx-lobbying-subjects&format=csv" > $@/subjects.csv


all: lobcon lobcon/csv expenses nomenklatura


.PHONY: expenses nomenklatura all
