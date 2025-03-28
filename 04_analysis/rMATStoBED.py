# Convert rMATS output files to BED files for the UCSC Genome Browser 

# SE Function
# Input: ID…1	GeneID	geneSymbol	chr	strand	exonStart_0base	exonEnd	upstreamES	upstreamEE	downstreamES	downstreamEE	IncFormLen	SkipFormLen	PValue	FDR	IncLevel1	IncLevel2	IncLevelDifference

def rMATStoBEDSE():
    rmatsline = ""
    while rmatsline != "done":
        rmatsline = input("PASTE RMATS CODE HERE OR TYPE 'done' TO FINISH PROGRAM: ")
        event = rmatsline.split()

        ID = event[0]
        GeneID = event[1]
        geneSymbol = event[2]
        chr = event[3] 
        strand = event[4] 
        FirstExonStart_0base = event[5] 
        exonEnd = event[6] 
        upstreamES = event[7] 
        upstreamEE = event[8] 
        downstreamES = event[9] 
        downstreamEE = event[10] 
        incFormLen = event[11] 
        SkipFormLen = event[12] 
        PValue = event[13] 
        FDR = event[14] 
        IncLevel1 = event[15] 
        IncLevel2 = event[16]
        
        #blockSizes
        UEsize = int(upstreamEE) - int(upstreamES)
        DEsize = int(downstreamEE) - int(downstreamES)
        MEsize = int(exonEnd) - int(FirstExonStart_0base)

        #blockStarts
        UEstart = int(upstreamES) - int(upstreamES)
        MEstart = int(FirstExonStart_0base) - int(upstreamES)
        DEstart = int(downstreamES) - int(upstreamES)

        # chrom chromStart chromEnd name score strand thickStart thickEnd itemRgb blockCount blockSizes blockStarts 
        chrom = chr
        chromStart = upstreamES 
        chromEnd = downstreamEE
        name = ID
        score = "500"
        thickStart = upstreamES
        thickEnd = downstreamEE
        itemRgb = "255,0,0"
        blockCount = "3"
        blockSizes = str(UEsize) + "," + str(MEsize) + "," + str(DEsize)
        blockStarts = str(UEstart) + "," + str(MEstart) + "," + str(DEstart)

        print()
        print("YOUR BED LINE IS BELOW!!")
        print('track name=',geneSymbol,'-Inclusion"', ID, '" description=inclusion"', ID, '" itemRgb="On"', sep="")
        print(chrom, chromStart, chromEnd, name, score, strand, thickStart, thickEnd, itemRgb, blockCount, blockSizes, blockStarts, sep = " ")

        blockCount = "2"
        blockSizes = str(UEsize) + "," + str(DEsize)
        blockStarts = str(UEstart) + "," + str(DEstart)

        print('track name=',geneSymbol,'-Exclusion"', ID, '" description=exclusion"', ID, '" itemRgb="On"', sep="")
        print(chrom, chromStart, chromEnd, name, score, strand, thickStart, thickEnd, itemRgb, blockCount, blockSizes, blockStarts, sep = " ")
        
        print("END OF BED LINE")
        print()
    return

#rMATStoBEDSE()

# MXE Function
# Input: ID…1, chr, strand, 1stExonStart, 1stExonEnd, 2ndExonStart, 2ndExonEnd, upstreamES, upstreamEE, downstreamES, downstreamEE

def rMATStoBEDMXE():
    rmatsline = ""
    while rmatsline != "done":
        rmatsline = input("PASTE RMATS CODE HERE OR TYPE 'done' TO FINISH PROGRAM: ")
        event = rmatsline.split("\t")

        ID= event[0]
        chrom = event[1]
        strand= event[2]
        Ex1Start = event[3]
        Ex1End = event[4]
        Ex2Start = event[5]
        Ex2End = event[6]
        upstreamES = event[7]
        upstreamEE = event[8]
        downstreamES= event[9]
        downstreamEE= event[10]

        #blockSizes
        UEsize = int(upstreamEE) - int(upstreamES)
        DEsize = int(downstreamEE) - int(downstreamES)
        exon1size = int(Ex1End) - int(Ex1Start)
        exon2size = int(Ex2End) - int(Ex2Start)

        incBlockSizes = str(UEsize) + "," + str(exon1size) + "," + str(DEsize)
        excBlockSizes = str(UEsize) + "," + str(exon2size) + "," + str(DEsize)

        #blockStarts
        UEstart = int(upstreamES) - int(upstreamES)
        DEstart = int(downstreamES) - int(upstreamES)
        exon1start = int(Ex1Start) - int(upstreamES)
        exon2start = int(Ex2Start) - int(upstreamES)

        incBlockStarts = str(UEstart) + "," + str(exon1start) + "," + str(DEstart)
        excBlockStarts = str(UEstart) + "," + str(exon2start) + "," + str(DEstart)

        print("MXE Event BED File:", ID)
        print('track name=inclusion"'+ID+'"', 'description=inclusion"'+ID+'"', 'itemRgb="On"', sep=" ")
        print(chrom, upstreamES, downstreamEE, ID, "500", strand, upstreamES, downstreamEE, "255,0,0", "3", incBlockSizes, incBlockStarts, sep = " ")
        print('track name=exclusion"'+ID+'"', 'description=exclusion"'+ID+'"', 'itemRgb="On"', sep=" ")
        print(chrom, upstreamES, downstreamEE, ID, "500", strand, upstreamES, downstreamEE, "255,0,0", "3", excBlockSizes, excBlockStarts, sep = " ")
        print("\n\n")

    return


#rMATStoBEDMXE()

