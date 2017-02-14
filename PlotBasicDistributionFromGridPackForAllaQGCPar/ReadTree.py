import ROOT

f = ROOT.TFile.Open("test.root")

h1 = ROOT.TH1F("h1","",100,0,1000)
h2 = ROOT.TH1F("h2","",100,0,1000)
h2.SetLineColor(2)
c1 = ROOT.TCanvas("c1")
c1.SetLogy(1)

crossSection=0.0
CrossSection_ft0_m0p1667=0.0

for event in f.tree:
    #h1.Fill(event.Lep1_pt)
    h1.Fill(event.Lep1_pt,event.SM_Weight)
    #print "=============================\n\n"
    #print len(event.Rwgt_Name)
    crossSection = crossSection+event.Rwgt_Weight[0]
    #if ft0_m0p1667
    for size in range(0,len(event.Rwgt_Name)):
	#print event.Rwgt_Name[size]
	if event.Rwgt_Name[size] == "ft0_0p0":
	    CrossSection_ft0_m0p1667 = CrossSection_ft0_m0p1667 + event.Rwgt_Weight[size]

h1.Draw()
print "Cross-Section = ",crossSection
print "CrossSection_ft0_m0p1667 = ",CrossSection_ft0_m0p1667
#h2.Draw("same")
c1.SaveAs("test.png")
