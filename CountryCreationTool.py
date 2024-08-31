import os

def create_folders_and_files(country_name, country_tag):

    common_dir = os.path.join(os.getcwd(), "common")
    history_dir = os.path.join(os.getcwd(), "history")


    os.makedirs(os.path.join(common_dir, "countries"), exist_ok=True)
    os.makedirs(os.path.join(common_dir, "country_tags"), exist_ok=True)
    os.makedirs(os.path.join(common_dir, "ideas"), exist_ok=True)
    os.makedirs(os.path.join(common_dir, "characters"), exist_ok=True)

    os.makedirs(os.path.join(history_dir, "countries"), exist_ok=True)

    country_file_path = os.path.join(common_dir, "countries", f"{country_name}.txt")
    with open(country_file_path, "w", encoding="utf-8") as f:
        f.write(
'''

graphical_culture = 

#如graphical_culture = middle_eastern_gfx
#中东middle_eastern_gfx
#东欧eastern_european_gfx
#西欧western_european_gfx
#亚洲asian_gfx
#非洲african_gfx
#南美洲和中美洲southamerican_gfx

graphical_culture_2d = 

#如graphical_culture = middle_eastern_2d
#中东middle_eastern_2d  
#东欧eastern_european_2d
#西欧western_european_2d
#亚洲asian_2d
#非洲african_2d
#南美洲和中美洲southamerican_2d

color = { 1  1  1 }
#这个不是国家地块颜色，作者也不知道这里的color是做什么用，建议使用和国家地块颜色相同的RGB代码{国家地块颜色在common\\countries\\colors.txt改}'''
        )

    country_tag_file_path = os.path.join(common_dir, "country_tags", f"{country_tag}_请将内容复制到common-country-tags-00_countries.txt.txt")
    with open(country_tag_file_path, "w", encoding="utf-8") as f:
        f.write(f'{country_tag} = "countries/{country_name}.txt"')

    history_file_path = os.path.join(history_dir, "countries", f"{country_tag} - {country_name}.txt")
    with open(history_file_path, "w", encoding="utf-8") as f:
        f.write(
'''capital = 
#首都地块states(带#的均为注释，无效果，若想要效果，就删除#)

#oob =
#军队数据，若暂时没有，可以在oob前面加上#注释掉 

set_technology = {
	infantry_weapons = 1
	mass_assault = 1
}
#开始时的科技
set_stability = 0.7
#设置稳定度，例如70%稳定度，则填入0.7
set_war_support = 0.7
#设置战争支持度

recruit_character = 
#获取领导人，将领（在common\\characters\\你的国家tag）

set_politics = {
	ruling_party = neutrality
	#领导该国家的派系，共产：communism，法西斯：fascism，民主：democratic，中立：neutrality
	last_election = 1936.1.1
	#最后一次选举（"年.月.日" （p社sb代码，无法早于该日期））
	election_frequency = 48
	#选举间隔（48为默认）
	elections_allowed = 
	#是否允许公众选举（no或者yes）
}
set_popularities = {
	communism = 0
	fascism = 0
	democratic = 0
	neutrality = 100
	#设置意识形态支持度，总数不超过100，共产：communism，法西斯：fascism，民主：democratic，中立：neutrality
}

add_ideas = {
}
#添加民族精神（在common\\ideas\\你的国家tag_country.txt）'''
        )

    characters_file_path = os.path.join(common_dir, "characters", f"{country_tag}.txt")
    with open(characters_file_path, "w", encoding="utf-8") as f:
        f.write(
'''characters={
#角色名称，请自行修改(带#的均为注释，无效果，若想要效果，就删除#)
	国家tag_角色名称，如USA_123(只能英文)={
		name=国家tag_角色名称，如USA_123

		#肖像选择（平民状态和军事状态）
		portraits={

			#平民状态
			civilian={
				large="gfx//leaders//USA//国家tag_角色名称，如USA_123.dds"
			}

			#军事状态
			army={
				large="gfx//leaders//USA//国家tag_角色名称，如USA_123.dds"
				small="gfx//leaders//USA//国家tag_角色名称，如USA_123.dds"
			}

		}
		#担任党派领导人时的数据
		country_leader={
			#意识形态
			ideology=despotism
			#特质
			traits={ }
			#不可用日期（死亡日期）
			expire="1965.1.1.1"
			#我也不知道这个是什么，但最好不要碰这个
			id=-1
		}
		#担任陆军将军时的数据
		field_marshal={
			#特质（如堑壕大师）
			traits={ }
			#等级
			skill=4
			#攻击等级
			attack_skill=2
			#防御等级
			defense_skill=4
			#计划等级
			planning_skill=3
			后勤等级
			logistics_skill=4
			#作者也不知道这个有什么用，不过能运行就不要碰
			legacy_id=-1
		}
	}
}'''
        )

    ideas_file_path = os.path.join(common_dir, "ideas", f"{country_tag}_country.txt")
    with open(ideas_file_path, "w", encoding="utf-8") as f:
        f.write(
'''ideas = {
#不要动

	country = {
	#不要动	

		{country_tag}_test = {
		#国家tag_精神名字，如USA_123(只能英文)

			name = {country_tag}_test 
			#国家tag_精神名字，如USA_123

			picture = 
            #国家精神图片（p社目前的主流是将其注册在\\interface中的ideas.gfx文件中后，再将其name贴入这里。其构成简单，你们可以自行去那个.gfx文件中学习）
			allowed = { always = yes }
			#想要限制哪个国家使用，original_tag = XXX 是只有原始tag为XXX的国家可以使用该民族精神。想让所有国家都可以使用该民族精神的写法为always = yes

			removal_cost = -1
			#移除花费（一般不动这个）

			modifier = {
			}
			#该国家精神提供的buff或debuff，可以上网查询id
		}
	}
}'''
        )

    print("所有文件夹和文件创建完成！")

def main():
    country_name = input("请输入国家名称（英文）：")
    country_tag = input("请输入国家tag（只能写3个字母，否则游戏无法识别）：")
    
    create_folders_and_files(country_name, country_tag)
    print("操作成功完成！")

if __name__ == "__main__":
    main()
#By bilibili：https://space.bilibili.com/355892829  Github：https://github.com/WGN-CN