import re

module_dict={'Hazard': [('4', 'rf_ra0_ex'), ('4', 'rf_ra1_ex'), (0, 'rf_re0_ex'), (0, 'rf_re1_ex'), ('4', 'rf_wa_mem'), (0, 'rf_we_mem'), ('1', 'rf_wd_sel_mem'), ('31', 'alu_ans_mem'), ('31', 'pc_add4_mem'), ('31', 'imm_mem'), ('4', 'rf_wa_wb'), (0, 'rf_we_wb'), ('31', 'rf_wd_wb'), ('1', 'pc_sel_ex'), (0, 'rf_rd0_fe'), (0, 'rf_rd1_fe'), ('31', 'rf_rd0_fd'), ('31', 'rf_rd1_fd'), (0, 'stall_if'), (0, 'stall_id'), (0, 'stall_ex'), (0, 'flush_if'), (0, 'flush_id'), (0, 'flush_ex'), (0, 'flush_mem')], 'Encoder': [(0, 'jal'), (0, 'jalr'), (0, 'br'), ('1', 'pc_sel')], 'SEG_REG': [('31', 'pc_cur_in'), ('31', 'pc_cur_out'), ('31', 'inst_in'), ('31', 'inst_out'), ('4', 'rf_ra0_in'), ('4', 'rf_ra0_out'), ('4', 'rf_ra1_in'), ('4', 'rf_ra1_out'), (0, 'rf_re0_in'), (0, 'rf_re0_out'), (0, 'rf_re1_in'), (0, 'rf_re1_out'), ('31', 'rf_rd0_raw_in'), ('31', 'rf_rd0_raw_out'), ('31', 'rf_rd1_raw_in'), ('31', 'rf_rd1_raw_out'), ('31', 'rf_rd0_in'), ('31', 'rf_rd0_out'), ('31', 'rf_rd1_in'), ('31', 'rf_rd1_out'), ('4', 'rf_wa_in'), ('4', 'rf_wa_out'), ('1', 'rf_wd_sel_in'), ('1', 'rf_wd_sel_out'), (0, 'rf_we_in'), (0, 'rf_we_out'), ('2', 'imm_type_in'), ('2', 'imm_type_out'), ('31', 'imm_in'), ('31', 'imm_out'), (0, 'alu_src1_sel_in'), (0, 'alu_src1_sel_out'), (0, 'alu_src2_sel_in'), (0, 'alu_src2_sel_out'), ('31', 'alu_src1_in'), ('31', 'alu_src1_out'), ('31', 'alu_src2_in'), ('31', 'alu_src2_out'), ('3', 'alu_func_in'), ('3', 'alu_func_out'), ('31', 'alu_ans_in'), ('31', 'alu_ans_out'), ('31', 'pc_add4_in'), ('31', 'pc_add4_out'), ('31', 'pc_br_in'), ('31', 'pc_br_out'), ('31', 'pc_jal_in'), ('31', 'pc_jal_out'), ('31', 'pc_jalr_in'), ('31', 'pc_jalr_out'), (0, 'jal_in'), (0, 'jal_out'), (0, 'jalr_in'), (0, 'jalr_out'), ('1', 'br_type_in'), ('1', 'br_type_out'), (0, 'br_in'), (0, 'br_out'), ('1', 'pc_sel_in'), ('1', 'pc_sel_out'), ('31', 'pc_next_in'), ('31', 'pc_next_out'), ('31', 'dm_addr_in'), ('31', 'dm_addr_out'), ('31', 'dm_din_in'), ('31', 'dm_din_out'), ('31', 'dm_dout_in'), ('31', 'dm_dout_out'), (0, 'dm_we_in'), (0, 'dm_we_out'), (0, 'clk'), (0, 'flush'), (0, 'stall')], 'PC': [(0, 'clk'), (0, 'rst_asyn'), (0, 'stall'), ('31', 'pc_next'), ('31', 'pc_cur')], 'register__file': [(0, 'clk'), ('4', 'ra0'), ('31', 'rd0'), ('4', 'ra1'), ('31', 'rd1'), ('4', 'ra2'), ('31', 'rd2'), ('4', 'wa'), (0, 'we'), ('31', 'wd')], 'alu': [('31', 'a'), ('31', 'b'), ('3', 'func'), ('31', 'y')], 'IMM_GEN': [('31', 'inst'), ('2', 'imm_type'), ('31', 'imm')], 'CTRL': [('31', 'inst'), (0, 'jal'), (0, 'jalr'), ('1', 'br_type'), (0, 'wb_en'), ('1', 'wb_sel'), (0, 'alu_op1_sel'), (0, 'alu_op2_sel'), ('3', 'alu_ctrl'), ('2', 'imm_type'), (0, 'mem_we'), (0, 'rf_re0'), (0, 'rf_re1')], 'BRANCH': [('31', 'rd0'), ('31', 'rd1'), ('1', 'br_type'), (0, 'br')], 'MUX1': [('31', 'src0'), ('31', 'src1'), (0, 'sel'), ('31', 'res')], 'MUX2': [('31', 'src0'), ('31', 'src1'), ('31', 'src2'), ('31', 'src3'), ('1', 'sel'), ('31', 'res')], 'pc_add': [('31', 'pc_cur'), ('31', 'pc_add4')], 'pc_jalr_generate': [('31', 'alu_res'), ('31', 'pc_jalr')], 'Check_Data_SEG_SEL': [('31', 'check_data_if'), ('31', 'check_data_id'), ('31', 'check_data_ex'), ('31', 'check_data_mem'), ('31', 'check_data_wb'), ('31', 'check_data_hzd'), ('2', 'check_addr'), ('31', 'check_data')], 'Check_Data_SEL_HZD': [('4', 'rf_ra0_ex'), ('4', 'rf_ra1_ex'), (0, 'rf_re0_ex'), (0, 'rf_re1_ex'), ('1', 'pc_sel_ex'), ('4', 'rf_wa_mem'), (0, 'rf_we_mem'), ('1', 'rf_wd_sel_mem'), ('31', 'alu_ans_mem'), ('31', 'pc_add4_mem'), ('31', 'imm_mem'), ('4', 'rf_wa_wb'), (0, 'rf_we_wb'), ('31', 'rf_wd_wb'), (0, 'rf_rd0_fe'), (0, 'rf_rd1_fe'), ('31', 'rf_rd0_fd'), ('31', 'rf_rd1_fd'), (0, 'stall_if'), (0, 'stall_id'), (0, 'stall_ex'), (0, 'flush_if'), (0, 'flush_id'), (0, 'flush_ex'), (0, 'flush_mem'), ('4', 'check_addr'), ('31', 'check_data')], 'Check_Data_SEL': [('31', 'pc_cur'), ('31', 'instruction'), ('4', 'rf_ra0'), ('4', 'rf_ra1'), (0, 'rf_re0'), (0, 'rf_re1'), ('31', 'rf_rd0_raw'), ('31', 'rf_rd1_raw'), ('31', 'rf_rd0'), ('31', 'rf_rd1'), ('4', 'rf_wa'), ('1', 'rf_wd_sel'), ('31', 'rf_wd'), (0, 'rf_we'), ('31', 'immediate'), ('31', 'alu_sr1'), ('31', 'alu_sr2'), ('3', 'alu_func'), ('31', 'alu_ans'), ('31', 'pc_add4'), ('31', 'pc_br'), ('31', 'pc_jal'), ('31', 'pc_jalr'), ('1', 'pc_sel'), ('31', 'pc_next'), ('31', 'dm_addr'), ('31', 'dm_din'), ('31', 'dm_dout'), (0, 'dm_we'), ('4', 'check_addr'), ('31', 'check_data')]}
lst=[]
res=''
cur_module=''
cur_module_lst=[]
while True:
    s=input()
    if s=='break':
        break
    elif re.match('    \w',s)!=None:
        cur_module=re.match('    (.*) ',s).group(1)
        cur_module_lst=module_dict[cur_module]
    elif re.match('    \);',s)!=None:
        pass
    else:
        module_port=re.search('\.(\w+)',s).group(1)
        tmp=re.search('\( *([\w\']*) *\)',s)
        if tmp!=None:
            port=tmp.group(1)
            if port=='' or re.match('\d',port)!=None:
                pass
            else:
                if port in lst:
                    pass
                else:
                    lst.append(port)
                    num=0
                    for item in cur_module_lst:
                        if item[1]==module_port:
                            if item[0]==0:
                                num=0
                            else:
                                num=int(item[0])
                            break
                    ss=''
                    if num==0:
                        ss='wire '+port+';\n'
                    else:
                        ss='wire ['+str(num)+':0] '+port+';\n'
                    res=res+ss

print(res)



# arr=[]
# while True:
#     s=input()
#     if s=='break':
#         break
#     elif re.match('\)',s)!=None:
#         module_dict[module_name]=arr.copy()
#         arr=[]
#     elif re.match('module',s)!=None:
#         module_name=re.search('module (.*)\(',s).group(1)
#     else:
#         if re.search('\[.*\]',s)!=None:
#             port_name=re.search('\] (.*),',s).group(1)
#             num=re.search('\[(.*):',s).group(1)
#             arr.append((num,port_name))
#         else:
#             port_name=re.search('put (.*),',s).group(1)
#             num=0
#             arr.append((num,port_name))
# print(module_dict)