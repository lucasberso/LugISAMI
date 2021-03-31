########################
# ISAMI VERSION: 8.0.0 #
# ANALYSIS: LUG        #
# Mode: SAA            #
# Written by: ALTRAN   #
# Date: 25/01/14       #
######################
MS.LoadMaterial('Al-7050-T7451',"7050_T7451_Plate","AIMS03-02-022","Referenced")
MS.LoadMaterial('Al-7175-T7351',"7175_T7351_Plate","AIMS03-02-008","Referenced")
MS.LoadMaterial('Cres-A286',"A286-Cres_Bar","","Referenced")
MS.LoadMaterial('Ti-6Al-4V',"Ti-6Al-4V_ab_Annealed_Bar","AIMS03-18-010","Referenced")
 
MS.CreateObject('DPines3','AirbusEO_DPin',[
['/CsmMbr_Name','S:DPin3'],
['/CsmMbr_Uptodate','B:TRUE'],
['/Diameter','CaesamQty_LENGTH:6,35;mm'],
['/Material','AirbusEO_TMaterial:Ti-6Al-4V'],
])
 

MS.CreateObject('DBushes3','AirbusEO_DBush',[
['/CsmMbr_Name','S:D_Bush3'],
['/BushInternalDiameter','CaesamQty_LENGTH:6,35;mm'],
['/BushExternalDiameter','CaesamQty_LENGTH:9,55294;mm'],
['/BushMaterial','AirbusEO_TMaterial:Cres-A286'],
])
 
MS.CreateObject('Geom3','AirbusEO_DLugGeometry',[
['/CsmMbr_Name','S:Geom'],
['/LugType','Enum_LugType:SIMPLE'],
['/Width','CaesamQty_LENGTH:33,4;mm'],
['/Length','CaesamQty_LENGTH:50,4;mm'],
['/Thick','CaesamQty_LENGTH:6,6;mm'],
['/ThickUnstudied','CaesamQty_LENGTH:11,71;mm'],
['/LugPin','AirbusEO_DPin:DPines3'],
['/LugBush','AirbusEO_DBush:DBushes3'],
['/PinOffsetX','CaesamQty_LENGTH:0;mm'],
['/PinOffsetY','CaesamQty_LENGTH:0;mm'],
['/SuperiorAngle','CaesamQty_PLANE_ANGLE:0;deg'],
['/InferiorAngle','CaesamQty_PLANE_ANGLE:0;deg'],
['/NotchedLength','CaesamQty_LENGTH:20;mm'],
['/ShearType','Enum_ToggleShearType:SINGLE SHEAR'],
['/StructureMaterial','AirbusEO_TMaterial:Al-7050-T7451'],
])
 
MS.CreateObject('Loading3','AirbusEO_DLugLoading',[
['/CsmMbr_Name','S:Loading'],
['/LoadingType','Enum_LoadingType:NO_COEFFICIENT'],
['/LugForceLoadingType','Enum_TogglePHForceLoadingType:RESULTANT AND ANGLE'],
['/LugCoefficientForceX','D:20'],
['/LugCoefficientForceY','D:30'],
['/LugForceX','CaesamQty_FORCE:10000;N'],
['/LugForceY','CaesamQty_FORCE:10000;N'],
['/LugCoefficientResultantForce','D:100'],
['/LugResultantForce','CaesamQty_FORCE:1000;N'],
['/LugResultantAngle','CaesamQty_PLANE_ANGLE:70;deg'],
['/NbParameters','I:32'],
['/LoadingRatio','D:0,1'],
['/NbClasses','I:1'],
['/Compression','Enum_ToggleCompression:Smin'],
['/UserSmin','CaesamQty_PRESSURE:0;MPa'],
['/PropagationComputation','CaesamEnum_YesNo:No'],
['/MLPDesign','CaesamEnum_YesNo:No'],
['/LoadRedistributionFactor','D:1']
])
 
MS.CreateObject('Law3','AirbusEO_DFatigueLawGeoDependent',[
['/CsmMbr_Name','S:Law'],
['/IsCracked','S:No'],
['/LawType','Enum_ToggleLawTypeGeoDependent:Fatigue Law'],
['/DamageCalculationMethod','Enum_ToggleDamageCalculationMethod:LOCAL STRESS ANALYSIS'],
['/FatigueLaw','Enum_ToggleFatigueLaw:AFI LAW'],
['/Orientation_init','Enum_Orientation:LT'],
['/Configuration_init','S:Configuration:AFI/thickness:50-200'],
])
 
MS.CreateStandaloneAnalysis('initiation_lug',None,[
   '/CsmMbr_Name S:Rod_FR41_STR4_LHS_Upper',
   '/Geometry *AirbusEO_DLugGeometry:',
   '/Geometry/ReferencedObject AirbusEO_DLugGeometry:Geom3',
   '/Loading *AirbusEO_DLugLoading:',
   '/Loading/ReferencedObject AirbusEO_DLugLoading:Loading3',
   '/FatigueLaw *AirbusEO_DFatigueLawGeoDependent:',
   '/FatigueLaw/ReferencedObject AirbusEO_DFatigueLawGeoDependent:Law3',
],
'Rod_FR41_STR4_LHS_Upper')
 
MS.CreateObject('DPines4','AirbusEO_DPin',[
['/CsmMbr_Name','S:DPin4'],
['/CsmMbr_Uptodate','B:TRUE'],
['/Diameter','CaesamQty_LENGTH:7,9375;mm'],
['/Material','AirbusEO_TMaterial:Ti-6Al-4V'],
])
 

MS.CreateObject('DBushes4','AirbusEO_DBush',[
['/CsmMbr_Name','S:D_Bush4'],
['/BushInternalDiameter','CaesamQty_LENGTH:7,9375;mm'],
['/BushExternalDiameter','CaesamQty_LENGTH:11,14044;mm'],
['/BushMaterial','AirbusEO_TMaterial:Cres-A286'],
])
 
MS.CreateObject('Geom4','AirbusEO_DLugGeometry',[
['/CsmMbr_Name','S:Geom'],
['/LugType','Enum_LugType:SIMPLE'],
['/Width','CaesamQty_LENGTH:21,4;mm'],
['/Length','CaesamQty_LENGTH:55,6;mm'],
['/Thick','CaesamQty_LENGTH:9;mm'],
['/ThickUnstudied','CaesamQty_LENGTH:5,5;mm'],
['/LugPin','AirbusEO_DPin:DPines4'],
['/LugBush','AirbusEO_DBush:DBushes4'],
['/PinOffsetX','CaesamQty_LENGTH:1,2;mm'],
['/PinOffsetY','CaesamQty_LENGTH:0;mm'],
['/SuperiorAngle','CaesamQty_PLANE_ANGLE:10;deg'],
['/InferiorAngle','CaesamQty_PLANE_ANGLE:0;deg'],
['/NotchedLength','CaesamQty_LENGTH:20;mm'],
['/ShearType','Enum_ToggleShearType:INTERNAL DOUBLE SHEAR'],
['/StructureMaterial','AirbusEO_TMaterial:Al-7175-T7351'],
])
 
MS.CreateObject('Loading4','AirbusEO_DLugLoading',[
['/CsmMbr_Name','S:Loading'],
['/LoadingType','Enum_LoadingType:NO_COEFFICIENT'],
['/LugForceLoadingType','Enum_TogglePHForceLoadingType:RESULTANT AND ANGLE'],
['/LugCoefficientForceX','D:20'],
['/LugCoefficientForceY','D:30'],
['/LugForceX','CaesamQty_FORCE:10000;N'],
['/LugForceY','CaesamQty_FORCE:10000;N'],
['/LugCoefficientResultantForce','D:100'],
['/LugResultantForce','CaesamQty_FORCE:2000;N'],
['/LugResultantAngle','CaesamQty_PLANE_ANGLE:80;deg'],
['/NbParameters','I:32'],
['/LoadingRatio','D:0,6'],
['/NbClasses','I:1'],
['/Compression','Enum_ToggleCompression:Smin'],
['/UserSmin','CaesamQty_PRESSURE:0;MPa'],
['/PropagationComputation','CaesamEnum_YesNo:No'],
['/MLPDesign','CaesamEnum_YesNo:No'],
['/LoadRedistributionFactor','D:1']
])
 
MS.CreateObject('Law4','AirbusEO_DFatigueLawGeoDependent',[
['/CsmMbr_Name','S:Law'],
['/IsCracked','S:No'],
['/LawType','Enum_ToggleLawTypeGeoDependent:Fatigue Law'],
['/DamageCalculationMethod','Enum_ToggleDamageCalculationMethod:LOCAL STRESS ANALYSIS'],
['/FatigueLaw','Enum_ToggleFatigueLaw:AFI LAW'],
['/Orientation_init','Enum_Orientation:LT'],
['/Configuration_init','S:Configuration:AFI/thickness:6-100'],
])
 
MS.CreateStandaloneAnalysis('initiation_lug',None,[
   '/CsmMbr_Name S:Rod_FR41_STR4_LHS_Middle',
   '/Geometry *AirbusEO_DLugGeometry:',
   '/Geometry/ReferencedObject AirbusEO_DLugGeometry:Geom4',
   '/Loading *AirbusEO_DLugLoading:',
   '/Loading/ReferencedObject AirbusEO_DLugLoading:Loading4',
   '/FatigueLaw *AirbusEO_DFatigueLawGeoDependent:',
   '/FatigueLaw/ReferencedObject AirbusEO_DFatigueLawGeoDependent:Law4',
],
'Rod_FR41_STR4_LHS_Middle')
 
MS.CreateObject('DPines5','AirbusEO_DPin',[
['/CsmMbr_Name','S:DPin5'],
['/CsmMbr_Uptodate','B:TRUE'],
['/Diameter','CaesamQty_LENGTH:9,525;mm'],
['/Material','AirbusEO_TMaterial:Ti-6Al-4V'],
])
 

MS.CreateObject('DBushes5','AirbusEO_DBush',[
['/CsmMbr_Name','S:D_Bush5'],
['/BushInternalDiameter','CaesamQty_LENGTH:9,525;mm'],
['/BushExternalDiameter','CaesamQty_LENGTH:12,73302;mm'],
['/BushMaterial','AirbusEO_TMaterial:Cres-A286'],
])
 
MS.CreateObject('Geom5','AirbusEO_DLugGeometry',[
['/CsmMbr_Name','S:Geom'],
['/LugType','Enum_LugType:SIMPLE'],
['/Width','CaesamQty_LENGTH:81,4;mm'],
['/Length','CaesamQty_LENGTH:57,9;mm'],
['/Thick','CaesamQty_LENGTH:10,2;mm'],
['/ThickUnstudied','CaesamQty_LENGTH:4,2;mm'],
['/LugPin','AirbusEO_DPin:DPines5'],
['/LugBush','AirbusEO_DBush:DBushes5'],
['/PinOffsetX','CaesamQty_LENGTH:0;mm'],
['/PinOffsetY','CaesamQty_LENGTH:0;mm'],
['/SuperiorAngle','CaesamQty_PLANE_ANGLE:0;deg'],
['/InferiorAngle','CaesamQty_PLANE_ANGLE:10;deg'],
['/NotchedLength','CaesamQty_LENGTH:20;mm'],
['/ShearType','Enum_ToggleShearType:EXTERNAL DOUBLE SHEAR'],
['/StructureMaterial','AirbusEO_TMaterial:Al-7050-T7451'],
])
 
MS.CreateObject('Loading5','AirbusEO_DLugLoading',[
['/CsmMbr_Name','S:Loading'],
['/LoadingType','Enum_LoadingType:NO_COEFFICIENT'],
['/LugForceLoadingType','Enum_TogglePHForceLoadingType:RESULTANT AND ANGLE'],
['/LugCoefficientForceX','D:20'],
['/LugCoefficientForceY','D:30'],
['/LugForceX','CaesamQty_FORCE:10000;N'],
['/LugForceY','CaesamQty_FORCE:10000;N'],
['/LugCoefficientResultantForce','D:100'],
['/LugResultantForce','CaesamQty_FORCE:3000;N'],
['/LugResultantAngle','CaesamQty_PLANE_ANGLE:90;deg'],
['/NbParameters','I:32'],
['/LoadingRatio','D:0,4'],
['/NbClasses','I:1'],
['/Compression','Enum_ToggleCompression:Smin'],
['/UserSmin','CaesamQty_PRESSURE:0;MPa'],
['/PropagationComputation','CaesamEnum_YesNo:No'],
['/MLPDesign','CaesamEnum_YesNo:No'],
['/LoadRedistributionFactor','D:1']
])
 
MS.CreateObject('Law5','AirbusEO_DFatigueLawGeoDependent',[
['/CsmMbr_Name','S:Law'],
['/IsCracked','S:No'],
['/LawType','Enum_ToggleLawTypeGeoDependent:Fatigue Law'],
['/DamageCalculationMethod','Enum_ToggleDamageCalculationMethod:LOCAL STRESS ANALYSIS'],
['/FatigueLaw','Enum_ToggleFatigueLaw:AFI LAW'],
['/Orientation_init','Enum_Orientation:LT'],
['/Configuration_init','S:Configuration:AFI/thickness:50-200'],
])
 
MS.CreateStandaloneAnalysis('initiation_lug',None,[
   '/CsmMbr_Name S:Rod_FR41_STR4_LHS_Lower',
   '/Geometry *AirbusEO_DLugGeometry:',
   '/Geometry/ReferencedObject AirbusEO_DLugGeometry:Geom5',
   '/Loading *AirbusEO_DLugLoading:',
   '/Loading/ReferencedObject AirbusEO_DLugLoading:Loading5',
   '/FatigueLaw *AirbusEO_DFatigueLawGeoDependent:',
   '/FatigueLaw/ReferencedObject AirbusEO_DFatigueLawGeoDependent:Law5',
],
'Rod_FR41_STR4_LHS_Lower')
 
 
MS.RunAllAnalysis()
MS.Save('Lug_B3_3.czm')
