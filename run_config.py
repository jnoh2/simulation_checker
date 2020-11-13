run_config = [
#{'c':['kix_kidmim1'], 'v':[2], 'r':[1,2,3], 'p':'CREB', 'd': '/oak/stanford/groups/rondror/users/lxpowers/simulations/KIX'},
#{'c':['PENT_MK6'], 'v':[1], 'r':[1,2,3], 'p':'GPR40', 'd': '/oak/stanford/groups/rondror/users/lxpowers/simulations/GPR40/ternary'},
#{'c':['LINO_BIND'], 'v':[1], 'r':[1,2,3], 'p':'GPR40', 'd': '/oak/stanford/groups/rondror/users/lxpowers/simulations/GPR40/ternary'},
#{'c':['MK6_G103'], 'v':[1], 'r':[4,5,6], 'p':'GPR40', 'd': '/oak/stanford/groups/rondror/users/lxpowers/simulations/GPR40/ternary'},
#{'c':['AP8_MK6_G103'], 'v':[1], 'r':[4,5,6], 'p':'GPR40', 'd': '/oak/stanford/groups/rondror/users/lxpowers/simulations/GPR40/ternary'},
#{'c':['M2_G11_IXO'], 'v':[1], 'r':[1,2,3], 'p':'muscarinic_xanomeline', 'd': '/oak/stanford/groups/rondror/users/lxpowers/simulations/Karuna/M2'},
#{'c':['PENT_MK6'], 'v':[1], 'r':[1,2,3], 'p':'GPR40_scratch', 'd': '/scratch/users/lxpowers/simulations_test'},
#{'c':['hFPN_APO'], 'v':[1], 'r':[1,2,3], 'p':'ferroportin', 'd': '/oak/stanford/groups/rondror/projects/MD_simulations/amber/ferroportin'},
#{'c':['trunc16'], 'v':[1], 'r':[1,2,3], 'p':'CREB', 'max':500, 'd': '/oak/stanford/groups/rondror/users/lxpowers/simulations/KIX/modifications'},
#{'c':['trunc16_K6C_N9C'], 'v':[1], 'r':[1,2,3], 'p':'CREB', 'max':500, 'd': '/oak/stanford/groups/rondror/users/lxpowers/simulations/KIX/modifications'},
#{'c':['trunc16_L11F'], 'v':[1], 'r':[1,2,3], 'p':'CREB', 'max':500, 'd': '/oak/stanford/groups/rondror/users/lxpowers/simulations/KIX/modifications'},
#{'c':['trunc16_R1A_S3E'], 'v':[1], 'r':[1,2,3], 'p':'CREB', 'max':500, 'd': '/oak/stanford/groups/rondror/users/lxpowers/simulations/KIX/modifications'},
#{'c':['trunc16_R1del_S3E'], 'v':[1], 'r':[1,2,3], 'p':'CREB', 'max':500, 'd': '/oak/stanford/groups/rondror/users/lxpowers/simulations/KIX/modifications'},
#{'c':['AP8_MK6_altICL2'], 'v':[1], 'r':[1,2,3,4,5,6,7,8,9,10], 'p':'GPR40', 'max':200, 'd': '/oak/stanford/groups/rondror/users/lxpowers/simulations/GPR40/ternary'},
#{'c':['M1_G11_IXO'], 'v':[1], 'r':[1,2,3], 'p':'xanomeline', 'd': '/oak/stanford/groups/rondror/users/lxpowers/simulations/Karuna'},
#{'c':['AP8_MK6_Gqa'], 'max':2000, 'v':[3], 'r':[1,2,3,4,5], 'p':'GPR40', 'd': '/oak/stanford/groups/rondror/projects/MD_simulations/amber/GPR40/Gq_complex'},
#{'c':['MK6_Gqa'], 'max':2000, 'v':[3], 'r':[1,2,3,4,5], 'p':'GPR40', 'd': '/oak/stanford/groups/rondror/projects/MD_simulations/amber/GPR40/Gq_complex'},
#{'c':['trunc16_cterm'], 'v':[1], 'r':[1,2,3], 'p':'CREB', 'max':500, 'd': '/oak/stanford/groups/rondror/users/lxpowers/simulations/KIX/modifications'},
#{'c':['trunc16_H602_prot'], 'v':[1], 'r':[1,2,3], 'p':'CREB', 'max':500, 'd': '/oak/stanford/groups/rondror/users/lxpowers/simulations/KIX/modifications'},
#{'c':['test_free_energy'], 'v':[1], 'r':[1,2], 'p':'GPR40', 'd': '/oak/stanford/groups/rondror/users/lxpowers/simulations/GPR40/ternary'},
#{'c':['MK6_FE'], 'v':[1], 'r':[1,2,3,4,5], 'p':'gpr40', 'd': '/oak/stanford/groups/rondror/users/lxpowers/simulations/GPR40/ternary'},
#{'c':['MK6_FE'], 'v':[2], 'r':[1,2,3,4,5], 'p':'gpr40', 'd': '/oak/stanford/groups/rondror/users/lxpowers/simulations/GPR40/ternary'},
#{'c':['MK6_FE'], 'v':[3], 'r':[1,2,3], 'p':'gpr40', 'd': '/oak/stanford/groups/rondror/users/lxpowers/simulations/GPR40/ternary'},
#{'c':['MK6_FE'], 'v':[4], 'r':[1,2,3], 'p':'gpr40', 'd': '/oak/stanford/groups/rondror/users/lxpowers/simulations/GPR40/ternary'},
#{'c':['MK6_FE'], 'v':[5], 'r':[1,2,3,4,5], 'p':'gpr40', 'd': '/oak/stanford/groups/rondror/users/lxpowers/simulations/GPR40/ternary'},
#{'c':['AP8_MK6_FE'], 'v':[1], 'r':[1,2,3,4,5], 'p':'gpr40', 'd': '/oak/stanford/groups/rondror/users/lxpowers/simulations/GPR40/ternary'},
#{'c':['AP8_MK6_FE'], 'v':[2], 'r':[1,2,3,4,5], 'p':'gpr40', 'd': '/oak/stanford/groups/rondror/users/lxpowers/simulations/GPR40/ternary'},
#{'c':['AP8_MK6_FE'], 'v':[3], 'r':[1,2,3], 'p':'gpr40', 'd': '/oak/stanford/groups/rondror/users/lxpowers/simulations/GPR40/ternary'},
#{'c':['AP8_MK6_FE'], 'v':[4], 'r':[1,2,3], 'p':'gpr40', 'd': '/oak/stanford/groups/rondror/users/lxpowers/simulations/GPR40/ternary'},
#{'c':['AP8_MK6_FE'], 'v':[5], 'r':[1,2,3,4,5], 'p':'gpr40', 'd': '/oak/stanford/groups/rondror/users/lxpowers/simulations/GPR40/ternary'},
#{'c':['MK6_altICL2'], 'v':[1], 'r':[1,2,3], 'p':'GPR40', 'd': '/oak/stanford/groups/rondror/users/lxpowers/simulations/GPR40/ternary'},
#{'c':['AP8_MK6_altICL2'], 'v':[1], 'r':[1,2,4,5,6,7,8,9,10], 'p':'GPR40', 'd': '/oak/stanford/groups/rondror/users/lxpowers/simulations/GPR40/ternary'},
#{'c':['apo_inactive_delN'], 'v':[1], 'r':[1,2,3,4,5], 'p':'CB1R', 'd': '/oak/stanford/groups/rondror/users/lxpowers/simulations/CB1R'},
#{'c':['AP8_MK6_G103E'], 'v':[2], 'r':[1,2,3,4,5], 'p':'GPR40', 'd': '/oak/stanford/groups/rondror/projects/MD_simulations/amber/GPR40/jpaggi'},
#{'c':['AP8_MK6_Gqa_G103E'], 'v':[1], 'r':[1,2,3,4,5], 'p':'GPR40', 'd': '/oak/stanford/groups/rondror/projects/MD_simulations/amber/GPR40/Gq_complex'},
#{'c':['AP8_MK6_Gqa_G103E'], 'v':[2], 'r':[1,2,3,4,5], 'p':'GPR40', 'd': '/oak/stanford/groups/rondror/projects/MD_simulations/amber/GPR40/Gq_complex'},
#{'c':['MK6_Gqa_G103E'], 'v':[1], 'r':[1,2,3,4,5], 'p':'GPR40', 'd': '/oak/stanford/groups/rondror/projects/MD_simulations/amber/GPR40/Gq_complex'},
#{'c':['AK42_state_C_o'], 'v':[1], 'r':[1,2,3], 'p':'CLC2', 'd': '/oak/stanford/groups/rondror/users/lxpowers/simulations/CLC2'},
#{'c':['AK42_state_C_o'], 'v':[2], 'r':[1,2,3], 'p':'CLC2', 'd': '/oak/stanford/groups/rondror/users/lxpowers/simulations/CLC2'},
#{'c':['AK42_state_O'], 'v':[1], 'r':[2], 'p':'CLC2', 'd': '/oak/stanford/groups/rondror/users/lxpowers/simulations/CLC2'},
#{'c':['AK42_state_O'], 'v':[2], 'r':[3], 'p':'CLC2', 'd': '/oak/stanford/groups/rondror/users/lxpowers/simulations/CLC2'},
#{'c':['M4_pose7'], 'v':[2], 'r':[1,2,3,4,5,6,7,8,9,10], 'p':'XAN', 'd': '/oak/stanford/groups/rondror/projects/MD_simulations/amber/muscarinic/xanomeline/M4'},
#{'c':['M2_F181L_pose7'], 'v':[1], 'r':[1,2,3], 'p':'XAN', 'd': '/oak/stanford/groups/rondror/projects/MD_simulations/amber/muscarinic/xanomeline/M2'},
#{'c':['M2_V405T_pose7'], 'v':[1], 'r':[1,2], 'p':'XAN', 'd': '/oak/stanford/groups/rondror/projects/MD_simulations/amber/muscarinic/xanomeline/M2'},
#{'c':['M2_Go_xan_pose7'], 'v':[2], 'r':[2,3], 'p':'XAN', 'd': '/oak/stanford/groups/rondror/projects/MD_simulations/amber/muscarinic/xanomeline/M2'},
#{'c':['M2_Go_xan_pose7'], 'v':[1], 'r':[1,2,3,4,5], 'p':'XAN', 'd': '/oak/stanford/groups/rondror/projects/MD_simulations/amber/muscarinic/xanomeline/M2'},
#{'c':['MOR_active_allo3'], 'v':[1], 'r':[1,2,3], 'p':'MOR_allo', 'd': '/oak/stanford/groups/rondror/users/lxpowers/simulations/MOR'},
#{'c':['MOR_active_allo1'], 'v':[1], 'r':[1,2,3], 'p':'MOR_allo', 'd': '/oak/stanford/groups/rondror/users/lxpowers/simulations/MOR'},
#{'c':['MOR_active_allo2'], 'v':[1], 'r':[1,2,3], 'p':'MOR_allo', 'd': '/oak/stanford/groups/rondror/users/lxpowers/simulations/MOR'},
#{'c':['MOR_active_allo1'], 'v':[2], 'r':[1,2,3], 'p':'MOR_allo', 'd': '/oak/stanford/groups/rondror/users/lxpowers/simulations/MOR'},
#{'c':['MOR_active_allo3'], 'v':[2], 'r':[1,2,3], 'p':'MOR_allo', 'd': '/oak/stanford/groups/rondror/users/lxpowers/simulations/MOR'},
{'c':['MOR_active_allo4'], 'max':400, 'v':[1], 'r':[1,2,3], 'p':'MOR_allo', 'd': '/oak/stanford/groups/rondror/users/lxpowers/simulations/MOR'},
{'c':['MOR_active_allo5'], 'max':400, 'v':[1], 'r':[1,2,3], 'p':'MOR_allo', 'd': '/oak/stanford/groups/rondror/users/lxpowers/simulations/MOR'},
{'c':['MOR_active_allo6'], 'max':400, 'v':[1], 'r':[1,2,3], 'p':'MOR_allo', 'd': '/oak/stanford/groups/rondror/users/lxpowers/simulations/MOR'},
{'c':['MOR_active_allo7'], 'max':400, 'v':[1], 'r':[1,2,3], 'p':'MOR_allo', 'd': '/oak/stanford/groups/rondror/users/lxpowers/simulations/MOR'},
{'c':['MOR_active_allo8'], 'max':400, 'v':[1], 'r':[1,2,3], 'p':'MOR_allo', 'd': '/oak/stanford/groups/rondror/users/lxpowers/simulations/MOR'},
{'c':['MOR_active_allo9'], 'max':400, 'v':[1], 'r':[1,2,3], 'p':'MOR_allo', 'd': '/oak/stanford/groups/rondror/users/lxpowers/simulations/MOR'},
{'c':['MOR_active_allo10'], 'max':400, 'v':[1], 'r':[1,2,3], 'p':'MOR_allo', 'd': '/oak/stanford/groups/rondror/users/lxpowers/simulations/MOR'},
{'c':['MOR_active_allo11'], 'max':400, 'v':[1], 'r':[1,2,3], 'p':'MOR_allo', 'd': '/oak/stanford/groups/rondror/users/lxpowers/simulations/MOR'},
]
