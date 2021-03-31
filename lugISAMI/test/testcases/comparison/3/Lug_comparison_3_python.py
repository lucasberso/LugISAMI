########################
# ISAMI VERSION: 8.0.0 #
# ANALYSIS: LUG        #
# Mode: SAA            #
# Written by: ALTRAN   #
# Date: 31/03/2021     #
######################
MS.LoadMaterial('Al-7050-T7451',"7050_T7451_Plate","AIMS03-02-022","Referenced")
MS.LoadMaterial('Al-7175-T7351',"7175_T7351_Plate","AIMS03-02-008","Referenced")
MS.LoadMaterial('Cres-A286',"A286-Cres_Bar","","Referenced")
MS.LoadMaterial('Ti-6Al-4V',"Ti-6Al-4V_ab_Annealed_Bar","AIMS03-18-010","Referenced")
 
MS.CreateObject('DPines1','AirbusEO_DPin',[
['/CsmMbr_Name','S:DPin1'],
['/CsmMbr_Uptodate','B:TRUE'],
['/Diameter','CaesamQty_LENGTH:6,35;mm'],
['/Material','AirbusEO_TMaterial:Ti-6Al-4V'],
])
 

MS.CreateObject('DBushes1','AirbusEO_DBush',[
['/CsmMbr_Name','S:D_Bush1'],
['/BushInternalDiameter','CaesamQty_LENGTH:6,35;mm'],
['/BushExternalDiameter','CaesamQty_LENGTH:9,55294;mm'],
['/BushMaterial','AirbusEO_TMaterial:Cres-A286'],
])
 
MS.CreateObject('Geom1','AirbusEO_DLugGeometry',[
['/CsmMbr_Name','S:Geom'],
['/LugType','Enum_LugType:SIMPLE'],
['/Width','CaesamQty_LENGTH:33,4;mm'],
['/Length','CaesamQty_LENGTH:50,400000000000006;mm'],
['/Thick','CaesamQty_LENGTH:6,6;mm'],
['/ThickUnstudied','CaesamQty_LENGTH:11,71;mm'],
['/LugPin','AirbusEO_DPin:DPines1'],
['/LugBush','AirbusEO_DBush:DBushes1'],
['/PinOffsetX','CaesamQty_LENGTH:0;mm'],
['/PinOffsetY','CaesamQty_LENGTH:0;mm'],
['/SuperiorAngle','CaesamQty_PLANE_ANGLE:0;deg'],
['/InferiorAngle','CaesamQty_PLANE_ANGLE:0;deg'],
['/NotchedLength','CaesamQty_LENGTH:20;mm'],
['/ShearType','Enum_ToggleShearType:SINGLE SHEAR'],
['/StructureMaterial','AirbusEO_TMaterial:Al-7050-T7451'],
])
 
MS.CreateObject('Loading1','AirbusEO_DLugLoading',[
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
 
MS.CreateObject('Law1','AirbusEO_DFatigueLawGeoDependent',[
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
   '/Geometry/ReferencedObject AirbusEO_DLugGeometry:Geom1',
   '/Loading *AirbusEO_DLugLoading:',
   '/Loading/ReferencedObject AirbusEO_DLugLoading:Loading1',
   '/FatigueLaw *AirbusEO_DFatigueLawGeoDependent:',
   '/FatigueLaw/ReferencedObject AirbusEO_DFatigueLawGeoDependent:Law1',
],
'Rod_FR41_STR4_LHS_Upper')
 
MS.CreateObject('DPines2','AirbusEO_DPin',[
['/CsmMbr_Name','S:DPin2'],
['/CsmMbr_Uptodate','B:TRUE'],
['/Diameter','CaesamQty_LENGTH:7,9375;mm'],
['/Material','AirbusEO_TMaterial:Ti-6Al-4V'],
])
 

MS.CreateObject('DBushes2','AirbusEO_DBush',[
['/CsmMbr_Name','S:D_Bush2'],
['/BushInternalDiameter','CaesamQty_LENGTH:7,9375;mm'],
['/BushExternalDiameter','CaesamQty_LENGTH:11,14044;mm'],
['/BushMaterial','AirbusEO_TMaterial:Cres-A286'],
])
 
MS.CreateObject('Geom2','AirbusEO_DLugGeometry',[
['/CsmMbr_Name','S:Geom'],
['/LugType','Enum_LugType:SIMPLE'],
['/Width','CaesamQty_LENGTH:21,4;mm'],
['/Length','CaesamQty_LENGTH:55,6;mm'],
['/Thick','CaesamQty_LENGTH:9;mm'],
['/ThickUnstudied','CaesamQty_LENGTH:5,5;mm'],
['/LugPin','AirbusEO_DPin:DPines2'],
['/LugBush','AirbusEO_DBush:DBushes2'],
['/PinOffsetX','CaesamQty_LENGTH:1,2;mm'],
['/PinOffsetY','CaesamQty_LENGTH:1,3;mm'],
['/SuperiorAngle','CaesamQty_PLANE_ANGLE:10;deg'],
['/InferiorAngle','CaesamQty_PLANE_ANGLE:0;deg'],
['/NotchedLength','CaesamQty_LENGTH:20;mm'],
['/ShearType','Enum_ToggleShearType:INTERNAL DOUBLE SHEAR'],
['/StructureMaterial','AirbusEO_TMaterial:Al-7175-T7351'],
])
 
MS.CreateObject('Loading2','AirbusEO_DLugLoading',[
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
 
MS.CreateObject('Law2','AirbusEO_DFatigueLawGeoDependent',[
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
   '/Geometry/ReferencedObject AirbusEO_DLugGeometry:Geom2',
   '/Loading *AirbusEO_DLugLoading:',
   '/Loading/ReferencedObject AirbusEO_DLugLoading:Loading2',
   '/FatigueLaw *AirbusEO_DFatigueLawGeoDependent:',
   '/FatigueLaw/ReferencedObject AirbusEO_DFatigueLawGeoDependent:Law2',
],
'Rod_FR41_STR4_LHS_Middle')
 
MS.CreateObject('DPines3','AirbusEO_DPin',[
['/CsmMbr_Name','S:DPin3'],
['/CsmMbr_Uptodate','B:TRUE'],
['/Diameter','CaesamQty_LENGTH:9,524999999999999;mm'],
['/Material','AirbusEO_TMaterial:Ti-6Al-4V'],
])
 

MS.CreateObject('DBushes3','AirbusEO_DBush',[
['/CsmMbr_Name','S:D_Bush3'],
['/BushInternalDiameter','CaesamQty_LENGTH:9,524999999999999;mm'],
['/BushExternalDiameter','CaesamQty_LENGTH:12,733019999999998;mm'],
['/BushMaterial','AirbusEO_TMaterial:Cres-A286'],
])
 
MS.CreateObject('Geom3','AirbusEO_DLugGeometry',[
['/CsmMbr_Name','S:Geom'],
['/LugType','Enum_LugType:SIMPLE'],
['/Width','CaesamQty_LENGTH:81,4;mm'],
['/Length','CaesamQty_LENGTH:57,9;mm'],
['/Thick','CaesamQty_LENGTH:10,2;mm'],
['/ThickUnstudied','CaesamQty_LENGTH:4,2;mm'],
['/LugPin','AirbusEO_DPin:DPines3'],
['/LugBush','AirbusEO_DBush:DBushes3'],
['/PinOffsetX','CaesamQty_LENGTH:0;mm'],
['/PinOffsetY','CaesamQty_LENGTH:5;mm'],
['/SuperiorAngle','CaesamQty_PLANE_ANGLE:0;deg'],
['/InferiorAngle','CaesamQty_PLANE_ANGLE:10;deg'],
['/NotchedLength','CaesamQty_LENGTH:20;mm'],
['/ShearType','Enum_ToggleShearType:EXTERNAL DOUBLE SHEAR'],
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
   '/CsmMbr_Name S:Rod_FR41_STR4_LHS_Lower',
   '/Geometry *AirbusEO_DLugGeometry:',
   '/Geometry/ReferencedObject AirbusEO_DLugGeometry:Geom3',
   '/Loading *AirbusEO_DLugLoading:',
   '/Loading/ReferencedObject AirbusEO_DLugLoading:Loading3',
   '/FatigueLaw *AirbusEO_DFatigueLawGeoDependent:',
   '/FatigueLaw/ReferencedObject AirbusEO_DFatigueLawGeoDependent:Law3',
],
'Rod_FR41_STR4_LHS_Lower')
 
 
MS.RunAllAnalysis()
MS.Save('Lug_comparison_3_python.czm')
