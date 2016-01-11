# This is a self-extracting archive. Copy this script into a '.py' file located in the root
# directory of Pythonista and call the script. It will unzip the data and extract all files to an
# immediate sub directory of the root directory.
#
# This file was generated using pyzipista (see https://github.com/marcus67/pyzipista)
#
# Zipped Application:    gitsynchista
# Application Home Page: https://github.com/marcus67/gitsynchista

import zipfile
import base64
import StringIO

zip_string='''
UEsDBBQAAAAIAJYBnUcptW2jmBoAAH9GAAAUAAAAZ2l0c3luY2hpc3RhL0xJQ0VOU0WdXG1z28iR&j6&YkpfLFXR9Np3yWVXV1dFSZTFRKYUkrKjbwHJoYgYBHgYQFpWKv&9_unuAQZ88e7FlY0tEpjp6denX0bWHv75PH6yn4fj4WRwbx_fru5H15b_G46nQ3Pkafz56kqfFrn91LN&rnNnP&7880dj7HWx3ZXpy7qy59cX9OGffu7xV&a2dM5Oi1X1lpTO3hZ1vkwqWqBnR&mi37P&va6q7S8fPqz8ql_ULx&_x9g&4K0k&56luZ1W9H7Vs7fpqlrb26woyp69KnyFFb4M7E_fPn786f3H&&jpo32aDowdvrpyVxBdqbdbV27SqnJLWxV2QQTaJF&aZeqrMp3XlbP07JyI2eDL1Hlji5Wt1vRmli5c7p1dFot643Lan563i3WSv6T5i00rLJ8XlU2yrHhzy745xS7_81i6ZDPPHJ6arV1Y3ttVUdoNHcb6wCD8t3Q_fcmF7Cr5Th__JTu7K_rSrIgby2KDb&yan6cTMV104qpv7dWODpNXZeKJ6Ir2Ygm73JVJZh&rOW1t7vV0dIY0r1y_lK1e6oS4XpG4sJX90Vb4zgSa37_nRzag09f0GDZtjkNb4Fk_KPGKaPS29qRCfXAi9aZLmg2kJdttRhLB5swfFozrKpNplemdjziY82mSfGcLeqe027J4KZONfVsXWLmu1kXpiUsbUg560tReZEoknU_LjdPXTilu53CLgnSI2DffmcDse_fpgPbEwdLcVy5Z9i_sfS5qu0hyPuvOCi3MeSXYkwCLglXr29rl9o34unXJdzCDmRoI6eErEFS6lStLnIYYoPLrQU&NtqT96YAP9SnK&IHqxSJNKiiFWSevIuBIOSJ7EjM6oM_eq_qUL6wJhm2MmPRKW9t0haXtW_rXF71mKzrLwqWvWKQuF1h6SYIpmWEvjuyvMuFF0ln6MXoVz6iidpSRXifds0TjQqjEIrnN3ZvQG&h_KToUlvueF2&NussCa3qsTHz2LJ1ZgVcrt6jEctgPepZK7iJelg6cWkCJvCxPzJinS0O6CpcFZrqcLV03kZVAODTaf5evCkilhN2WfEB5qm9m8k5nF7JonyUVL75wZZXQgemJLX2ZztMsrVJ1Q1hZOGqOSjTmZA8UKfs3xTJdQX2ZFbf0hfs12WwzekifOLqcrxdrmwSWE6&WDlZn6Kcq5ROzy7ArRwvxPjW5gZdU9Y_0I6WlcmIO3ErLBeYrzMhCV&tiZfzunjrTKzs2sF6japF60bcm0jxaZ0Aq0dDh16QS9MwmKANFGrggXlUUhv6VliaIBjbsjmkJ6T3FteqNZFq5rf&Fnn_84FglwbTLdVJLc&7pgvhHdq5qEkWrt3VKTAWPPH_ZuRcyc46CnmO2hsFeLGFa8wNHIRZjvB9TPcg8cQiycAkkxt6T3K0eBavCWOhAovBsjUHhVeEMM9yFyFxDcX1Fr&lGFOJN84LeLxGEdrwln64Ta0gQo9VBiGHiU3bD9PnGYReXeYkF24T8MVGYgz6j3sLHGkTkqsiImLegHKxAIc5jx4JEkuZJ1qM95EiIMcQIiuwbDqVlsawXQgbHEEiXtBMLkGvOIHpIIVrLaDh6Rw9s64oDjKjLLb7Odj3eJHZPIKlaE6KgyE17UbQHLysKIXx6jY1bfF0hzJLewbeyB3kt0iXvv4R3LOXEFL_COiAwknEmwvQmcOIQab5MX9NlDaJsMWdHIps0cIYsPreOdHPB1sZxaN0uQ39TGHJVUu766jRJJ6AuJGZWHub4JlkCy9hF5hKlkFigBxLzmzcQaimqqar1TtEGvDx9DL43zyUM1voBgm0h&8ZyOT4VdELxmlgThkIn6LXuS3XdiLYtBAysCiDAE&jvx_h6Npx8mdrB_MZeP4xvRrPRw3hqbx8m9OPj82j8uWdvRtPZZHT1hK&4wS8PN6Pb0fUAH2DLn&qMoo7BJtVN5jwdRzDNW1F_VzcBlEgy9CYBnxCIt1miygsNaX3QusgQaXyyU_y7ITRKImidyNLUTTAShgYgfRxr9EUGZ49C3xnBa0dc7BkGMA35HCOiM4B6doKkoGd8lHkips07h9XMxlHQsy7lI0ffYA2sS6SmryQ_UjZeRYhvD5wlb7_IgadMC52ctpVnlW2q252V7bYoWScYWfSMEtAkGTgBnH2sPz743yZQL_FIcH6WmMnIUOvkBSw7vyM3SV5hRSzuNS9gQwbyi6wGkMcWRQ3FJ3irX_cmSMaexbufAYYO4dfVTNjfJctl6dhnJt6eUSA5I&UekK9&FbRQKF_Bsk4ZSeeQjCyBQlu0LNqh6nAp&pYhWl35lO2fwimtHlQlgetcmbLOD1ivHjrAHrfsKXzj1cipkk8oNvErJgLuRQ7sveINIVsOCOxT04rDoz1QNBN2Pief6LbAYTlnKOS_QNzcEVhnL0bnPELxRd98E7RjGyUra2BvrOWxSwhCzSGXhZOw8LEviCbZ&Z6MNgA3Xeadj0ENxBsjbWDoNGcL2VBIqAmVkfGRz3ctGDZgzTZd1EXtM9mdfA47dtJd_mQLQ6doQ4dgwKBExk_Z1tLU8_ghFlmSbogrRHSAAZf2u3NbmAQ0QKGekdd8CF8AQ0iVO55QskAcPpl7l9MuCGx0tmZpg2cYUba5YoQKuqwjReCjBMem_5gkK0i6AuLap0lUjZQk7WEkq6CGXO1658k4MtVrMeaQu8lOgvZ2ukqioLHYqofBmRusFIExROBfQ5YeEDRrzqdWcxTs8YpyqvK4wgSPqZ7NiGejJ2oOkhsh96Qr7mlgFT2NUSe79q4jVAdvj4SSqR7uo0nmZLdH9JJUg9D3xjlREjmFd1FQ&0VCdHLRZgSLpPaSTjQAcpVmEj4XxFtmLJ0R5q0qx2t4_FW26ZBwMr&F58gKwQMtkXqp4slTChXmB3SwboIBzbIRv4g5alma55JPxzJvFJz5W0ZjZdWEdf7MS6jDufZcoAqW1_D3GIMXK2REHXhFPiLRXRJwIegzQhRbY1oum1WgQKeQQAj9cvzFRcDxDetDoM9JrxhkEsRdSp2GUwWUqsoEYYj8jB6eHC052ChBFFZCR&lLklSJkBq8MCwCqsevRwsyYkxzJQj1pnJJkbaEt_AskahL4eRLCIWAEhRa9CnPi5q8C6qEGoTZKDoezx71eAkvoB_cToTOAXApmekFBNboh1qB0NG8cNFWL7jSxhYfYXzR_MBtFhevsG8wGkZdloX4heUsZ76FfU3d255P5FVahHc_&HXh2F39ggDbCdmVd9kq1B_DDIg2XgKxjkN6ownCfCkZ5B2W98SJdTxQOM0hQvjfOi2lHiMr7i3WvzBNDYUf3UiBgetzGkwadeUtW_vgxNSkgAL0fUIpofVOizDMH6SW&IpgoZOW2eOwhDrEHHQkvshpNa7qAhmVDBBb2IGHvSPjg5phA69wb0MsfkVOVsEQYhMUwQLwsIX2UNPiWnZ7zoIiW0M_W9KeP_LaR_L3tkb9ua6aF8yezvlkE3GF3mbPw&mmeBjJTFLfiSlmP6awX43xpsYsWSMkiPpWcEKmywGpBbelEcn5BAMELEwpxK_ojqvoDURb6jYBY9YcLKQ0Qh9wIirHKt1LUi4pFrD86SX7higthbIZvdiL2giglEvxVeMvlU8ci4CLolog41RfmbiMRI9Jclei40EggImVogA9d2lJSmvOG9qtOLsx7ldXSiocimhSJ0I5IzvK7Ch&KkpCcxkqGyGb8keRAJ15lCOzSKX3s4GjS15ewKWwrKY8cg5w5dhCZh9qsX&kD38ARC7wc2Jfi6xGfX9FSa_vipLyKnXp7fkE_rZOaF4G9xdRJ16TdRpJytEg9x8&Rur7R9inHhmkxNKAfj5dIEQV83_gvhLq4SS9RV2xvwEgOxJ_zTRY3Eem4ZNlEHUKQ5EzQPlMbUrKG8SBFj4NFhSSt0ArpL_NNPBZ5jjUlVJf5ji4IcsgAPUesRxECn5qc5Ce2nyw2qim8AMgKKGmexwWsApvQasVm6RMSf&rUCRqC4aIOQLGLomFvQaQHZ4saeyJEXfPviZZKssRzzLyzhXX4uRcO5eU3LRpswrGR_wQdj3F4wqgcnS2pBidS2_PcZE2u0KCgODnygC1lXGxvvY4CAvveYV9jkchel84HTkw7pP4_&tkcJr&cpJ&QwaLU9qV5mCBeIooZWV4qoGZBSShf68ndeLIgChcPEsyoiUXf6YoRtu6Uh1YcSkxBxCFp6Ss7aDaEaoICHp4v6Evhlq&bbx83gafJo3WISsnvpRS3bHTeh6iw1y4r8il0yxbtU5FCmJCC7cIRRybJnLiITTmtGrbTcyIn9wcveWcISZaCnKN6cvuhneXLUNv5oAu_pw2qZEqpW3SQoldVntOTBLvi0Ua6mFkAgkU363SPJW6K9IsfV78cJlupbmMgG1C&AJxqZbJGPagWp5lSQwc2hPRKe9I8K9gOrCd8VvHEncBy&YOzhObC7f7EDW0HIfOHjcKm0pPg2nj186RtUu1UFcmHs05ATGQ00VrCZvkH4wANqTRjE7P5YSg_DupscsEmni48Qs9oaEYVUrO6ne_IujGNSY43u75kSgRV_uccQvT3GxlFLUnaqFcZ_5yj4L86gAtRKsDYkUWgM6NlslY0Yk_Q6vz1jqwweg40bY0awNXqRXVhrcs4Dq5ZlC5t8CB9gW4zWCUF6Mvasb53hyDlR0viYYF8HH9so58e6rdc6lxbraUM0VDJ9Eie9WiiBkMGf6zhQxQIikDSbGGsj8uoQt8jUFLB0oYUVQor&t1izIup08a6YM3j5AKGpsoL5FSbCvDEOeNwWBxcvvTu8N9osUkKshto6RGFKg0liGIpJBjpwV6hCzTmGHgLxA094ca3yoVK2ZG6LizdBEgAkCLKoJNKy4MMaRlO4jTEMaWw1JCdgNXHAigdBA9L&rfqs7EsWRpQqkji_4PIrqQ3cW5JjRyW_2lYD5FSTL0qVlzdPKCfW1zfGBi1nC0M1_Q4EvRttvV1YIeefATgkE1qPL7nQ_ZwkHCm4SkrOR_3Tqdp5UU6rPkrWnka554eB5Zh2JLgTb1fCc9Mq5WdPD1Xun_XMuLJ0vsF1LaQe9x0WiN7J9oSbcj44rxKzrWqDeGgaP&T49PKG7IN3tM3MtwdOrhj33polTpxik__RHS&40TV&F8w54BqfIjQw7WGDyaCT1l&UaGRsSIu5XEqNcf6CLrZldUobPtTvRFwzSFuqeUAoPWLVd1yd2qzuyJpmBtSf2dbXJN9a3qAFiviRVrbnD1TdeSdFhFQBIltvT&C8iptUBtKEXemM_xl5D9V9_OVhLXuZpCJtr0BRADKGn&R7184UqeYJQoOZX2syEgioDjwkMrlWfoHqBcY8_l8bxJdfRQW9dkrrXzFz0TaSFjYeYjKwJ051xHYXAooYqAHwMSypbDxq2nvghhGkN&ZCaVAv1miz0b6UmzTWwZ4QKlT_zbRMbT78r0hY5C4fW4ol8oGPcY4CH18ummzshMnbSKpH1BMeRFYWXr9U3ctInm9hzJkovv0Wsa_Q_ECOQdFPOE7ekEwOGQUhKk2wzSFHUmOE5GSG1Z7ChL2L3n6YLIuCOYEHYh5yeot_CJnKJpr2mDZUlhYYFpDS7aNz9RFsmggs4hR2TPw3mFDn9CGYiqwN45MQnYWepQcZzjx_ZwhuinlwhaTTWIhfwD8gXCRS2fg3oU&XPtMgBpyYUxVJeLUToGeRJ6eQkY46LOEvK0abmoN569tni4eZK1LtzFy0czqUZqkqGbEh6KmhJ7M6w6S5mLCpl4W&RPR52K27Yu2YMdKbmRZGqNz&yTWH00iOLboQqU_UlVd1o842pdmNnTUp3UDdJqp70gw7VsefKyu&k60YQGp4soDD0_HarBoV9KXbHSicw2v_6IWDB&rymvmhSqD08iIX4rwxlB_7dckAfDrP3CcnQFPd9O55gXTHWQWYvX0W2aTPwNDfySO5AY9DsgyS1N0HZ2XZqS8GCi_vMil3q3Z8fJUy2LKGVLCCzxS5daQ623TbOX56k_LItcBLCk6LPkIVOeurJ_zToDMMjhvVMraGgN9LXOSImU4ZNmWkLdoEZCccTrImVMONuzmlhNeToOhGIXFPd51ulNc8Q5scG9igHM3WG0kqjqqwP3jCj3p37orO1XKT7o&Ouew0p9NDuB5kEYE_W0qITP0twUqtIq&3zXtrXiLF1cdItGDgaJ4BQ58fIdOg6zAHboyXIpVQfoAEn7xeHx7Zrb550jRhMvFNakEWfEDzdH6cmQZlJ1X_1cFpBiTs4YYEOZgGkZIZ6j9rqBWyIi5tKZWiQSXCNXTBi&IANGg8SzP49IJDMnpQzlRe09zovlwYgBS&XnPo&BnJxJB6fC6EXpXlNu3YrIMd78Kpc2vFHZnxhOFwgAEAtror&peFOcLV6DbQd6SQE_hW8n2v02LXmAPRSZPOxW35DLE6CQYCfmFuiFpSMVy9jDy7QRb9HMUkqTgxSRhyEZW_tiEBWqq6g2QoQk45oODbcYnsjrzdyV7aRoSI25lrPiXH3v2YM8QjxlNE2ngfYMvhtTWmVY4azXJnEcscOARls6j8qnXTwdJsRCfzAQVZRhZKCzVRBwO6MHdTBH1OHg7G07Q5iwO8aCvRbZrhlgKQLMD68gNT1OzbHLGTK39FM&YMcwjRpZB0OFg_ETHoQT9xvPo3rt3nUseA9Ti6Zxgxgm5rrhweg0PdB7m0grMmyCQNONjN3cb3B_b7tT9nrJlzmKjYORecPhoCkx_mb2WS9sIIYx37mEQZZHKr9sacHw_EuRZGzdbHvla1A7QQXkcmoZ7KX32xoAfxSu_nQu0MhKxaZoUnZcAZLBhiU5GA0jzSsv4k_y3W9chBo&2G_DyWQwnj2zUnzs26vh9eBpOrSzu6F9nDx8ngy_2NE0zMne2NvJcGgfbu313WDyedjDc5MhnojXwtRstAA99cA&D&82G45n9nE4_TKazWi1q2c7eHykxQdX90N7P&hGLB7_7Xr4OLPf7oZj84Dlv42InulsgBdGY&ttMpqNxp95QYzmTkaf72b27uH_Zjjh_d0PtDu&aB8Hk9loODVEx9fRTfdQZ4MpkX1mv41mdw9Ps4Z4HG4wfrZ&GY1venY44oWGf3ucDKd0fkNrj74QxUP6cjS_vn_64dHgK1ph&DAjPtHJiM7ZA7MmPBtWJ2JoffNlOCH_jWeDq9H9iLbELPHtaDamLXjieCCUXz&dD_gQT5PHh_kQNR2wkBYhhk9G07&YwdQoY&&6NGgWIu7SGl8G42sW1J4gcVz7&PCEUELnvr&BAyY8AEYN7c3wdng9G30l8dKTtM306ctQ_T2dMYPu7_14eE30DibPdjqcfB1dgw9mMnwcjIj9mJqeTLDKw1gczqc_hEdaMvwKHXga3_O0k_Ffn_g8RzQBaww_k7aBmZHczbcRbQ4J7Qu&x6&QF63wn0mNHuyXwbOMaj_rehCZzSx3VytIKVrtHFw9gAdXRM_IySJCwBCI6GbwZfB5OO2ZRgl4ax0v79np4&B6hH&Q96R6JOt74QpZ0V_fIEX6QBexAxInjgY9VJHBBqFr46AjtPe_XZ63e_&pH&Ti&mEKZaNNZgPLFNPfV0M8PRmOiV9sToPr66cJmRaewBtEzfSJjG00ZqEYnJeteTS5CfbEfLa3g9H90_RAx2jnB2IhlmRdawQSlGx60WMdsKNb2ur6TqVnO1b7bO9IFFdDemxw83UEzyP7GLKF6Uh58qArKB9PeTs6Lb99ZMC&_8adDFMNOGuVSuyMgQJ9_AzPPCZUpOHQ41UNoUuKwFmxpSiusKmdtoyuxOksn0bVF74y4itDuYqU02rfBCpJATUzR2qBogPXrtdIRQQdyTQ8B6u0Mt2gIcGyueOD_aVOETS6PNr0lEOZMVyiC6Xbqkq0M9ViqGbkN0BMKVcQRzhl8skKRwPFzdub8DBPAXIrCt9oKwYNxOZ6qVxakclCQhKvbqetLUL5XvFcO5LMkz5Yitfway64MAIMQwEM9s8a3HBGwD&X8pbdFpwq8cQOz&vxQWtpTvCFSAAAYpJq1z_XTpqbRMe&_JPuXet&YuzgX&Qc1siTjfuXvMf5Z3RnqCOvy_ZCY0dKAnPb_2AyJ1kdH_o8dre4nb&2HYDYzOSdRkTtdQm5Xx42uW_bXrzKeXcW_uIQKPePMyDuuGq_tcbwjrRmqwZdkVkQK3syFUKZSwjYcCwhaF829yy0I8hl3IwHA8PgJiFqLLEfe4m5vyP0Th0rBq&wAzbLBXK_uIuEyuvRUUCP9bKdl_iMg&xIfuiByZStdCtbXl4icSVd&Z1YVy&681r&&s1_XEHBeBLKAfE0CCpm4kR5iEAuVwIZOwyllUVOZ5JbgAT0yXelmZQ4O4MZnTnUXvBw4fpIAlaWzehuln4Xf2h4zpGeY&&i5e5EZ6KVjMjp4NTnnND0q8D4oOJ&&Lm3Z8swZQsbZrAuucr_2wtKG&Ta6OBq_nBPiOL_OUbDl6wVqhC22pGK&50vrL6967eGse8R2ujB7txl2Ad83XMQvILemGoKRSH3uoy3W7yLCenLhMp6t0VGx&2sdrY70Mc0NG_rBofLtp07JJ2E8eQts4cVt1C069Huxy1ij2rmDpUM9Na480sJGZcSoitOR0nTG0tSkWcPMHdmU9CS7xdEwXeuYGxcXhPD3Ma&f4&SHmfNvk6lg9tc89e7InpYnsHDDWR_xJFPKXb02nm47N5MHevbG1deWLm_XRqPXD2TnkYuc_toKuO6XFuFay&anLX3UQKCSFcmx_14L5c073QePcG4xDajsMHDUvwO1FRuVTwXu2K5y134lR6IavNds5GMAbUEsIUAY6gT1s1pob9Hev4OjTAeDSRr9HKL11sdSMG8i79oqme02Z9Bjb1LFt9dyU7wnzIxgvvepCWzHVkaxc_e&Uhoq0wz&hUlgB3yRQ_&o8On4SbXV9IgreCe8I9NQUU7RG0xA&oTy5fLGCa6&Nr8noGmnVbGrihBM7Ys0IuGs5mX9EpTjTFhDJzvYcLxS7TiNqNQQr6Vh7jiHaMKum&GT4wuHqpF4hTewjRouMm9JEgW7skc&n4Lc&z3WxwpYv4fUEsDBBQAAAAIAEAGnUcxkLdxYQIAAG4EAAAWAAAAZ2l0c3luY2hpc3RhL1JFQURNRS5tZHVUwW7UMBC95ysG7WFbqc3eQOIGqoBeoFKRECd24kw2Vh3beJwN6dczYwcoRZx2bT&PvPfmOTs42cyrN6PljM3dmsfgIYfgYAgJ6lqPZA8KLsn6kcAFg4KxjhgWm0dAeC8&cweJYmCbQ1phDJypB6mI8IW6GzwDUzpTaptmt4O3yNbAu9mbbINHZ&PafB6ptjdhipikOm69epvIlLI5EUEYnrLbKCSaQqbnUL3&Hx5wm2EJ6YFBViss5BxcoO_Bw4AJRmS55VboiMQWKnK01yVkIWo&3QPGCHstYf1JSMd134KKqPwtS1PL0AdP0K2&dgWq97OdpCROkcF66IJoUMLcwkdaQGnMsS&Uq9HihwDQ80Apya4dRPH3WdT2LdwHUMpSV1DS0svA5hhDymWUWgF6cqRewzJaMwKPYXa9iKv8JvQzOlEbNjK8iuCJBSAVqM5fuEuv7Z9OwVDKKPQrRYNe62lnGR4LyZkVaE9eSxRQnf5doo38RD5z03wNM3iSGxK1Ec9ULNoSuU3NOCtYMUtcc66olvlO4qtTAZhhzDny68PhVMLYit_HCZOZ_eWrAyGvC3U9nlu4c2hqBzbJxqwTkL66cZT00nVE84An4uOfNLXwxvdXRXOYE9MVrM8p&5uv&bQ5oKX&Dsrv&FywqFDmQnxDKECOioDLathtVY06wKY8FBYaRqPWl4njGa3DTuaM_myY3HBNPyQw8r6k52Zl1VudK6E4drN1&eHph_Dbo41tXI8t3ITFu4CiUA4qXnM5BOfCUh_B0EpzecIy&uA1DOqI5tB6of5BjRlm&6L5CVBLAwQUAAAACACWAZ1HmgB6rxAAAAAOAAAAJgAAAGdpdHN5bmNoaXN0YS9idWlsZC9naXRzeW5jaGlzdGFfaWdub3JlS88sKa7MS87ILC5J5OICAFBLAwQUAAAACACWAZ1HC8Yq9hYAAAAUAAAAIwAAAGdpdHN5bmNoaXN0YS9idWlsZC9weXppcGlzdGFfaWdub3JlS88sKa7MS87ILC5JjK&KLNArqOQCAFBLAwQUAAAACADtBChIg4PeUfoDAAC5DQAAFgAAAGdpdHN5bmNoaXN0YS9jb25maWcucHm9V1tv2zYUftev4FIEojDDWF8H_CENXCTFkA29YhgKgpZoj41ECiTdJf9_55CURMl06_5heogl8ly&8&HwRHa9No7Uun8uZHi3zkh1GL5utdrLwx&cWGGKYbHVh6IwotW8ofBeFcWh1Tve4sYB5cIv2eDCWvdCMVwBsxRk65ZbS15xK4JxqndfRO2qX4uCwNOIPTkId6&cjYNQdkcnLLWi3YMAiY8R7mgUaaV1aDFRe6V1K7j6YdXm2PVz0fiDa2s2bq_Ie_5FkFwzpngnGCM&k3JdVqki2ky1ap&qivTcCOVYb8RePi19zVEkyRM&9toQ_iieV_Qrb4_iIlJFyxBLI2vH2Fo60VmaZDy_cACFYfhQGJ8F4IVrdAgOLFdTVqMefoLKLHRIGaRHkRc9kMZNHsYNuU&cQrS0BLlyRcodFAp&gW5lEiyJ2a8bsTseaHltN9e2JNeE_jBWSE8akq_qUUu0VqQ2kqJ52VXIIZYpMjCw746rphVmIqEHzJePSSUB0VkFGaDbt9yJGHMxulvsA2CLlUk_OrA1V8yCV6lVdBK&HnyqnW5EOxwLLL3ucRNhTD3uZSvWYQvZPhoYNH0RlHaJurc8UiY5HFxaQbZPtfCi9Cq4OBruNdETZuW4VBbsALayGcyWWCcfWj1_X2Hhwv4st6pKQluGlT3FCUWC&EesK4Ac2tX62PdQxBNYwBadYRqUE_qMAUSDG1K_LMkI9rT6&u2HbXbjz_277Pqnm7u32Y03N&nlck7hcDY9JkPcK&LeAPMT3mfC&yVr&fXNb_&y8T&8flbh9i6vsb1&yG9cksJrDqf1&Nk94eB95FkkBbS_R3A30C1ln96fsu9iSkwBZomaQD2j6vyeSmjqzHOaFrS9gbLw_l_YehbQwfQYK0Tr4ZtQJNySy1BWx04YWYcL5v9DmWSeEfmUIGcw_AE8i9h_jeANS1RiC8ZXFdrnGMTpxez&xKtKqr2mV2gOOhHJtEwPGzbwsDfBNvhKporlPTLdxxGlZaZAqHRIW6cfNK8Sb4snCKkLLZS8IB1&FBEkS2qYzkBNWenk13Bzxdg3fliE61n0_JKPORBRGKMN64S1&IBhPmg1DAbF4oRgVJYhhBjPMlxcp38NYH2uprsDVuikW5GfNuTlxJVlAFdbXCD&&I2wfadeWJ&B4_ko9s3zdcatZ8HFvqmfdEQ1EZJEWCHtmYfB7fJIz4QC7cMYEY_Fp1V2mIgCvp1NWH9Lbah8ZqaYnWXg4nHHRiotB9DURZUceXC0GJYmuVVictLJ9o6Tpnd7wXiz7HX5GJeP34j&a8R0090CGxBcGI4OE2cPI2noLBJHz&iPBV6qjHUQEGP_bg06RfEvUEsDBBQAAAAIAKWRK0gnYyyCdgAAAJYAAAAkAAAAZ2l0c3luY2hpc3RhL2V0Yy9naXRzeW5jaGlzdGFfY29uZmlnVcoxDsIwDIXh3aeoxA5FSGzcgq1ClkmtJmoaR4lDlNvjhYHxve9fOr9X_rwAOIvzuHJUmh7T7T7PAEuxtwaVMqxIdLDRFrSO5HyoShDFUcRM6k3OUPgQ5d__&KXUVLA6SiZXOHUpe0gbOskDO_3cssGzNAb4AlBLAwQUAAAACAAiDSlIbxYY9AsDAAAKBwAAKwAAAGdpdHN5bmNoaXN0YS9ldGMvZ2l0c3luY2hpc3RhX2NvbmZpZ19zYW1wbGWtVU1r20AQvetXTJODm0NVQ6GEgg_lJiXQlkASSglFrKWRtWS1K3ZWNu6v78xISuR8HAoFX3Y1897MvHnrU7hpLAH&DJBpO4dQBl&bbR9NssFDbfmqDhG2NtHBlxydTA6&Qg_dMyVyXhm6A4QakiBpvPUp8BGzU6hsxDKFOEZwfNc5Ww7gqTEJDgy1D72rwNl7BM5Unhi8&YM5Q9w06KGMaBJnezCl5lITYir7BHubmuPquBzjK2WTcrxpcWL3uD9ukPG1ZENjfKQEnYmckzDm8N1wTdRH1Dp7koYjOs7dIccxdR1Dq7kujG2NXAy9tUdVURltl95kQ1OCxbiEKVm&pSntJ27WZsfXcccFZHd73FRm91uSjj6B9vX28gpYnfWPaz2fZcPHlRTjmkBpltfxxMBUVUQiyOS0Ol_eLyXiliZA0dr0XIhPo0w5fAlty2cIPG47yngUAg3Pb4OsU2XJbBxWecazioq4goSUCjkL1ZUh2odY&T_mbkIcmabz2NiwmA_ayoYldE7BUwgOmrCHti8bMA2aSnWwLT4XQ2xiefOQN6iicTVhwVT3LKD6YDGFEmJLQrXBEdZA3Tsh63mtrtUfsDOu19388HG5nIB5o51j8DJE8Y6W&2wyqq_uLumyj4UOF43ZqY_JF09ytB3ewbbjqrELZVNU6JLhgQlxlt1FviUrPtVF_xa2VvDn1nkMyWaySvT6wePz_LnRrderq0Nq2NZcyexdSBExh3UAH5IazPG0ZJ6L94s80z4LNdq&EAb&gpfggjfuiVwzMpAvPEHP5WQR25DwKfFn53hXUjSeaow0eH_Q4rghUX6AmGp4_J5nU36RQjEGreAm9vgqxStQwvIS_zHFEPHI8PX2kufjDp&EWqE1Yi3nDvA24rszKo0fDPOodw6XtarDT9WTVWDf8HvJOy55Hit59FrjewXcIFtcHkx5BMU8nEWWPZtnwlwo1woujKOhdaJefWfSy_aT94w5Ngc4mat4wn5CLw7b82vdd3zZtvoPMLhsAMjGlEJSijHygT37C1BLAwQUAAAACACWAZ1Hvk2692QAAACEAAAAIQAAAGdpdHN5bmNoaXN0YS9ldGMvcHl6aXBpc3RhX2NvbmZpZ1WLSw6EIAxA95zCE8huTEzmJJMJqVihCWBTygJPL3Hn9n1_AQsKpL8BZreToNdT_vSdAmntxUeqCo9skgaOqlxXa4eObZv9mW0G8a1_FvtaLmJ3UMICGce3NUr7q3CjmLkbcwNQSwMEFAAAAAgAyr0qSBqCkErVAgAANggAABwAAABnaXRzeW5jaGlzdGEvZ2l0c3luY2hpc3RhLnB5rVXfa9swEH73X3F0hNhQRLfHQAqltF0Z20rT0odShOrIiYhjGclulv9_d5bkyM2PvezJp5Puu7tP38lqXWvTgN3aRDlT2ySYpV4EM9dVofqV3VY533cNtq0sZd5oE5wbbVaqWmBYvU0SI0st5ilmyILt8PpllGPgGx4IWXpvnCZLAJJkLgugLQ&GC1VKLqo5J4A0clZiLbMJxQAsSv0uSmJgIY1z_ZNLDC2lgal3sOvu892547LZDG23m2ZUS6N1yaMDPUYAZUYO69wrz5XSYRAaIpDdZXrCdfo5hQ9ozJYa6_wonNlcVGkWduSfXNYN3HQfpSsQFmQU59hg0hht0rPdsZGFeWuQdSC8MxiBbUwqMwdsZNOa6h910FX8zzoQb1hHJ4ONWMm25hv5PhcfqB3zgTfmV54vf&8w0Cu3bd2JeDpwsxe3uEZ75k58QjuKxA6Wkjm12kaYhi9aleZLma_4O3tCmj2RFit8fevFaoM_CuX17guzHdmDwnYRKLYGiynFGmvzSBMvaSNrbRUO3JYNol2J5yGvl53CyZNVeihPBpdwASh7iHt0l3z4mg6AvF68MXcqi4WhqkKTLlRDWmg0iI1Q_IaJsnwX_QoKo9fg7w7o8hhjZ7FYIWhtADija6GQu_f7EFFo43sGVYXu96XqAG51S&12h1ojOs2OR3ZMYCjWfYrDyHuwfnr8_tRDEAsQ4MvBkY_Fw0Rdy8q&quTJ4kwnJrKvZUg_zWbXHGyW_HhBbXQurSX69gmg7lM&rOfHeICeifDo_6b7n0DX&cwv0vBWhk1n7Bq0&bOwFgopOT5ezsZsaDCNNHHyYCvpUOf4F2XCLD4ymE7h28Qzg5v9zuvXN9ZNt92oZjnQNHu4erz6ye&vfv1_vOEvVz9unh_yLHC8exJuRWm9KCRak579Y3_4KDeF7YJ2mE_mdb8WrJVzYptz6mHMOXHD_ZgiHE107C9QSwMEFAAAAAgAdQInSMJ8IqMJAAAABwAAACQAAABnaXRzeW5jaGlzdGEvbG9nL2dpdHN5bmNoaXN0YV9pZ25vcmXT0svJT_fiAgBQSwMEFAAAAAgAZgMsSGu5PGaNAQAA3wMAABMAAABnaXRzeW5jaGlzdGEvbG9nLnB5nVNNT8MwDL33V1idpqQSjDtSLwgGSAgOgxNCUda6baQ2mZKMaf8e9yvtNrggRW3z7Pf8nDqq2RnroTZlqXQZqZPtqpI6r9G6EXdHF0WLsjZbWXdJaCGKcizA7FCLgcaT2wiA1kliD6kCWL9noPSQ4XoGgEW&t3okELSAzKL0OGkMVdPgsUT&0mGclcq7o84q5bxkSUgObRDr82uCHTHxG2s_St0&3H08Jr3RUDkz2pkaYRABegExoW6p4A3kuN2XxCiqmau1qvGpZ&C24Zu5txUB7Aoak2PKDp3TovrTzr&MZHMzG0&sZrSTdOHLcs_v67fTaoWxjfS_O&fwPW9yxDhbcukyrxpMHFzDkneGtAz7Bp2TJe3YUELm_UyTnGdV8DXphozpjH4NBknqm7TOpmVFkbH7rGqlFpeBohr_&BBSujA83ng53Ye4zTib0Xb4PTofhj4M6OmVmITRWmN5&E6jALSkhg6JZykHaXXLmpJggOKkK0IPuklCtCcsBKQpMCEaqbQQrPXRO4qiH1BLAwQUAAAACAClkStIOiPUY7EBAADYAwAAFQAAAGdpdHN5bmNoaXN0YS9wb3B1cC5weY1TUYvbMAx_96&QZRxJoAt7HIU_lNvdVjjKGN32KNxYuTO4drCV2_7fz3bdLt36cBAc64v0SZ_kvIPeKW2fljDx8P6jEPowOs8w6dkVJ9ZGCE&GSdUUuxXi0&3D_vvjDneb3eM9rKBeK6VZOysNbOzg&EEmqxaiNzIE_OrGafyh6deds_ydMeShOfF3&3xoYSkEgKIBELXVjNgEMkO7jChAPsI0km_u0C4gu3bnyK2z1B5j4ocuC6nHFFjPYB2LRqbfjC_RLirK6KCtwjDtE4b7V7TyQE2d3DJyDpoz7SdmZ99AUxx74wIVgtORpD9Lqwyh7FMjs&4kzSry8z7ooYBdIoVVHMUF79G1lJbydxlv2oLnF5lAJ8fRa8tQ&Vx&2262n5dwzA&1bajBOi5lqZsKbueZ53SeePIWPszVjJ6iNxcdqXFRDb8aWtXhmYjrBbDmaF5s1gJytWjknsyquktGdbEG&8_uS7fY_YRenUqXE0WPGffbduosIhVeJpbEMQVuclnxyauFL31McIUqN&7kciasvkhj3E11Xe&fzdDpj0jtRsyjRjxIbRHzmI9ViD9QSwMEFAAAAAgApZErSCI1C3QxAgAA3QUAABcAAABnaXRzeW5jaGlzdGEvcG9wdXAucHl1aa2UzY7TMBDHX6XyCaS4yuc66S1OU0DiBCs4rFDkJk5rrWuvEgcWqj4LD8OLMW5TaJoWIUp7cT0fnvn&ZvqwRaVkbYtm6IPgX5CDmDGNWHaGw90WKbbhYHujag22JSsfV43uVFWUWuoGLO9e0fSFO038OCKeMz54U3f&eQnhRihzHniwgn9IYns4_g8CuWJLySs0M03HoQzdVLy5mun8cJqplvwZQtAOjs2ht_3WdSbuzplswyBxJkEQ7nbgqXRlJXj4LRDtjNFqJFGtoatWfINcXjSqtX&w7b193HoutQRjzWQL1l7e5T5zUUrdcvArdaOgv4ZVomsPWW9omZVGQNkz1HJZT9dMVZIX&aWDuk5AOSgNae7O0xiHbprjMCU5TjJK8SKN4pzSxPNp8scBsLDDwBkfhgNgpO33fbmWgv&4ztUQhE_SaeRM&Di2ODwfwITugMannfN&gNC&4CHKU4kiNw0SGlGc5S7F4TwkOCauh2kYuSSLk3i_8NBNpMSGrXjR1wB47PstFrolWMACNhtmoWHdGSkUx4F&Iuloou_shPuBjqbRdQ3v_bO5uPnXUI8W9PLKMilWasOVgTjJa2OvOqNhtBu_n73CfH2yxSp9JNEjIzdpeJn2x9dWKmj1n3L2RGz8Z5CqsDAK_wts7ROXslzz8lGo1aAnXglja&k1XP0cJQs&8hdBhLNgDvuWBylO7ijBKU38lHhZFgSLS38CA8BBfCR85_9XhoRnjOH7E1BLAwQUAAAACAClkStIMNqaOYAOAACJQgAAFAAAAGdpdHN5bmNoaXN0YS9zeW5jLnB5vRxrb9tG8jt&xZ4aQWSjI5Le4T4YUIHAeRnIOUXsw6HXtAQtrWw2FKmSVBzjev&9Zmdn30tJdp0GQURxZ_e189rZVarNtu0G1t&1SSUfl3XFm0F9a&X7odpw9bwqB25&r9vr66q5Vl87PTDwzXZd1fr7xdAB3Nn7RFNrm3V1beFRj&1dsyxoNOl43ZarFIYz9SzZNF8RUn_1ZmdJ8ubssjh7c&7_w6vi9dm7V2zBZvl1NVTXTdvxmRi__PH89O3ZxeULHw7ABK6bqh&KIjrh9P3567M38QmSg1mSvHj58uzy7P35i3eKwA8vLi9ffTi&QGa_BZCLf&3ww4dXFxfuCKCDseu6vSprVDPvkkR_wjg85O2WNwUtQArCLuuy79lrUHraXv3Kl0N2kjAGf1d8zYqiaqqhKNKe1_s5a8oNn7PtzV1fLcu6kF_vyp7T40Ys8pz1u6tCrGIPJM&bBt5UPSljtXhd1j1HGkiFMYE6F&MBWnyYlw4hGHW_GzDNAIDoZzOMTMEQfprXNpP62QwbjmHcfFFsC_XA21XVgcba7g4VBFLheMeHXdf4ZP4ilWFjKIp_6Ei7pBKaO4EVWkx7FFl8AiHxAVyIj2k&YVOWas3NI&qaazkMk9ncF26Ofpovxb_pUVeWSTYFk8t2sy07LqUoru4Qeyq_PZ8z8fEdsk6MLzdbOUaMIQA_C5RkbWdI&KxZt4dtTiAQagJzta3GNXH9ulqzmjepPYl9z57JiYxty2HgXUNDsLLp7JcZe2oTyTu_rcslT2f5bD77mM8y8_bb2Ry9z3r1sQGoJ7&&MssAzeyJPfT7L08E&Cwj4pLXvBJiT047DkFxZamC3VbDjeIQ1HnNv7DZtJ_JpXb5VghxvSTgAibkYqWEH3vQTGuHg_udxCYLw1RAxrrJRiznt1cAVG1wKKy26eNAvimH5U2Kkx0XsHmhWRgaJAG5vMRBIVQGXFpmMx4gMzW33223He&7yOwgdjpx8MVyCdMOW2bXtkMBur4JopkeEeuing0ekXK80EFhVMAtZMgUPtcMxb7ICSvQtIOZqdSpX4jQ5vCTBHb4DngRriA8gGmetOFpVNLmVMD86WfphGCxEN&cVUKKKKL1Pm37XKDJf22rJtVY58zLtRR4Imn0weijuZrorNuOgak3ULfkNRADBZjZmdKnkwuCdWGAI1SEFWPTdUYwUZkikIHxj8I4Ru5CmZAn7GBMQRoOYkYn4YC&ITVrLuR&qQ3DYKp6oS0Hbm2DKu3h_8PsGnAWFBB6yA4aPqAxDONaxqmktKFTmUclhUtjhBX6QK9ZyOpJhDgkozOA63sidUA_eJ55FRSxpiuXxZoKqYVYEliNwi_rFvrJqaxCURAmL7dQ8q0wJ2YmeFDMNWWPCf2YDfkXMNSegpMf5WiyMgWCNbZgBzrbTSU2eoMMUcnkp3Mnw9j8uHPJvuQ7SnuuLVTN0FIidObGcrKKhRJOLq4KhPZcywBIEVZu8ZjJxpKdNYVKBFJaX34GOl27UWybJQAbCAohrBpEUZ9KiMnt1SRjZY&sn1iGkN921QBGqUsIZ5EsNe1fcotSB5TA2GH&5Kx6z8lkHc5lXSkRgt3sEEAOpWTgVHoa97axbj6JcBPwBqjkiGN8lM3&za9elp_tnG4e9_T1W361Kj8XcsdopXlMzE6u3215l&pEZI2d5RqrqRNMheDQAIN1vtti7&VFe_ejfFG8wwrdUAQ&0pA&PfuZLcROcTZafEWMNeR5v8&&keLmQHn&aBWPXLd71zyPX_zoIiSi5bqP1SNrW_AFk5tAk7OWbTNUzY4zWztjZrLWmzNEfbDUGalKNI0jKpgo7GhpYKCJx2_2EKYGktqoRO&0wbpn9yo_DIWvXISo3foxZQhjqnHx7D6FCRMpYrccCpqM23t4tcV4SzqCUmRaztl0xaZXbPojm749mf7zZHrBpv_ZhfQRxeaTjOgGudjw&u0fzxR3QSkkhb1vMaRUZMohv7_0_HPKoYdl45G4RQFoxa921_nkovwsAhA1IYaWQtGJbOtYmQIBCtKs6oXm6iG1uwGR2LHbyt6mwTLXyI&M&ftkOsTdKF_r9rZBzmwlWlWZqywVrmdaSTMmOKZ5rsZUuho6W_z8mg_fy3rHU4i4RxcpR6znbdk1QmuT07IReQmQkteImE4JBk1qoquaI2qaiM78GgeR_N25Auj3sve1qpYDtefw_bs5W96UzbUMxkhHsCiBhXMR8PNMJCKDIoeScdOnxBilX9nfM&5l5SU1LHE6uL6zEpRhJW&4bRE45vP4ZgybiWBsBudPhtjPdshPBSOpZtRqgYqUI5uSVoCAgrlZkVxyAb8nIPxmR3ub9027qtYVX40IYIOuOGzkNN_ODAku5NCVTb&mXeEiTS0k4CvtrlvSYpdUbRrMpVPZRrZUa5JdrMu4HEGHCSXy1KhTpSYPMo0LjOuEoV0tk1OTXZLwGBBFHSaioqrHJHmvua3RuwNZ5rNFWsmDQD6CIabkcCt5L8o61IySxHcy_CTk2NoetIN8NVPo226AMijqlXPR0V9EzwC8VqQyEi8oqGLUhC2tJP98R9WmMH8jHtw6OtCrVUxo68qyJOTIMlvF1TdBBBf9_KqFDe5abwkqKK4wrEPhiCpid3w4YUts3Usz3ZTNrqzrO2GnhglFxJM9PAAQ5h5uQELljNqWzAtjE_zo_Rj_9odc7c&1sj0Ohu6124pD6YK4EAP9UG62j_tkkgjsBdQUUawHnHvbhSw2UWWNTfmJmxdgryXMCMmQF4BlarK4fdUvYPs_iFw1ngWyQ_A6ROgq2o4pemp4XqH9RMDFJfWMVnupXA&TmZP42h0kb8SFR2oCVdVIb0ZI0dlnf&2eLWWVJkkyveZR3&VcN3FsDtQZ59tPcyCxifl2YeHWFY5vImbhlxIe4hFKKvyJTXvhqHT8q2k5h7iWpTvvPT4y7UkRRzS_tD&1moxFDbdTtI9jDnbDGwDKnEyrRZ5HO1bpDQb_gTthxYxMWscdM9etENBx9I5v2oEHrn5gVyQbAB4yvHvhvTPgISE8z&VfjreyJKyVSeQ2fdfxSRYlEycQi0QjFFGaQwSNyFEFxMlZM61oA&Mt2wqFOgaUipg0S_w9mHqrjTK6jPvCry9rXOWHUdjro8uYcH8XY20eJzcf0Wa2D&VeJCMUHdyk2JENTQHpXc4K4sDYFiguRMhXafXfI07ltKnD8voYxkwt&lV58jSGpdRDdBauzigjY5wfUtpRvHlqe2y2qJaTQFYp5&MzWvM92mISQ9eQP5uuaNfGsq5AXnnlJ2CLmlbi3lKcEavUYk8NXKjGSE02zg5VMA9gxysUD&Dkl5WJvl_Ety47&tuu6sb5kHj3a1SwsAdMSZrhXTBT0SndIB&9brMpzUU_u2hVd_ZcfvVekj7UzT2Z76BMu_K0VVyx6WpO1tefwBdze__AXPMjxTLsmi2fxxYU5HSUJXb8IMlkRBErPpRVHXoPvYcUNjnnt4RLtM3kAi_x4O5FvYpHg_pSUX8ycZR5nJlbd&YMXfX0lE0_Nh_bd1iDNIqXE&axUTI53Y0DxExzb4SSGJrQJUHvTmpyhFS_txwvmpr5IPliPb0HCqmmBsLujUBHCfpBVq7HLeI_co_7iofD2H2ku8c6HiT8eAtJgYEmSx&FQ4lYgUq9QP3a3IVI3L6&2b3bRe9&&_e1ByxZYptn6o87jTx9yqdUMMpobh0I6vHMhDvrrA_HpOwo&Gq32VKpQgiqZsWbYfEs3uZJrON7izlnz2QubE9gZb4ljHjwla7VPhwPsOO9SpsnWzSJR1xPlw9P2d&V1kZugC8gnF_2bX149zsAVGH&CMLfnfsA4ljYexVstNRuTJ9O4yDvurZj7l14t1IpN2Epad9D8QmLI_a2r4TSzJUAG2u&LJsA4779e8DjIK4z0nKogiBgQ57Y5bued_59DPVG3Q84NFNP3MIq3rbd6tBEBUcT3UMzi7pzT8BCbr33LybR_eMpfqR7uQA6n3k3Z6JXvtjPL0DMNSPOn23XDu2yrRezm2HYzuYMUFbru6Lva3lHaM6WvBvoHpGSbaEe5lqshXowV&3CpszrSl8NO2hacr59BBvt2wR3zrzrZAfpEFYkRGZJ9GLOZTe5juthGXxeZ0eUHFSx6S67CT0B8bDl4WGk7HcflNEWSJRRUzFozEEyjXB7oHZwCIkXMnBjpAbILCpntFh7MFdj6f5BrAXl1ZFsHVdp&RGWHqaue5RHh5mT_6UvS74d2Cv8ECcGZc_4t7PDdFAM&IsIiAKBf30YAdLJK0wbqx2eqomkc0JEDQLnpzsqzZhhtTkud_IQLJa2xN2GgyFET8f9mVYJ3onAyTdlX0im8T6E3uCKExLcUeriA4eQE6uAwqQKpOOd&HiGV2nTjV8SaoyYM9Hi2b2dakAH86uD0SxtqUn3p3Tnz7peF9je3o5hdszE0Ubovtljza3MtdH7yov47imu3et7iMCx_XtSm2s&xziqY36Woyam5UQWvq__dNiI&Grz2M5VqJiwh2TjNQa_D6EUL8KWqJ1NJDmMw59rc3q0SD6So1ppEU&2rNiORcZIVSvLjbNWK8stfOPggHZiE_X1PqJOoImsaCBz5uLufRNVTJEJ9MRQEmox0oc7GApNu9CyhNGfoOwRRxG34nAif47QrOzwYl1PX8zyfKb2mHIU&V6U5frclmaprwldQ4Rdr7zIAw8ILzfu_JjR7&Nuy&qTfZl_aLfiJunisttB2Q&OICSmfcG6rev2tq6aT73zs0lVXajbB5qIlTb0OCSnsV&uO3ftHUHVJUD3B3daPgWXMeseZ8iXj1XSo7dQ&Kxq&D0&hfhT&HgrX9v&l0EuOgByNKVqrPR28S5O&DVPYVFPDcPKDmgJlaAOQm0u6tfgEjZRd9ogeaXKREJTotmVaE8ImkWBl&mLYlNWTVHgpX6JIkn_D1BLAwQUAAAACAAiDSlIGzme71UBAACEAwAAGwAAAGdpdHN5bmNoaXN0YS9zeW5jX2NvbmZpZy5weZ1TQWrDMBC8_xWCHmxDCIZCCYUcmpZCLz20hR7Fxl4nIopkpFVCft_17DguTluo0UUzI2l2dq32jXUkSmtqtUkSh9pClXXbPElKDd6LT1w&weExgj03X4HHDsnvEyF4VVgLKZVRJGXmUdeRiJQQNz406LLxTTMRRfPhTK9v0blHd0AnliLVtgS9tZ7SCxs9L8WiWBQXMPAZA3tk4tUaHKm5hqN11YTAxpZbWaEmYO72rijOhttaNkgvhh6InFoHQj_uySEFZ0SWtk7SmUhHV6WcWx&cG8NekXWnX8L7K7po9WphMRrZAG0nlMO9JbzOkQPja3SSrOx0LPlw4QdJfGWigMCUL8Ew8wzajyjOeqfMRpa2Ockj7DA0g_iS7cpajWD_yHfqtU17Yq8FB0ft5ooH7osYvr5B7ydT&neuu1pxXcGBy&v2j_TjRpxHgEWTecj5heQLUEsDBBQAAAAIAGYDLEje9YRM8AQAAJoTAAAdAAAAZ2l0c3luY2hpc3RhL3N5bmNfc2VsZWN0b3IucHnFWF1r7DYQffevUBeCbZqYfjwUFvLU0qe2FFL6EoLQ2rO74sqWK8nJXS73v3ckW7ZkexMnUAoha0szZ2akmaORed1KZUjHk4T7R9oZLvyrkCf&2Mq2a5NEgZCsyga53L_j4PjsJPMkOQl5YMJinEAlSf9L7u1AIVtoqB3hzSlD2VIwrcnDpSkfQEBppPImir85vPwsG6OkEKDyfUII&lVwJJTyhhtKMw3ieEtapqAx9Lm8&0M24ASdKCG6a0FlIfotsTp5MUKMynmvgbOFdsJQoUwFn9FziztNuzhRYzHhViHVaI7qwV6av65HBl9tWCcwdDRdywpcfGE8&LjuYA_4HxAVmE41oQ33A0LPRRyYtaQfV3CfksExrml9oaw0XDbDmmtACRX6NkLaCeuSFUyC8Hpwr28XyUgpND6biwBclFSfAUyKoE5tlkbT7oyqqBO8_MWcJA07CHjGNKLRnpDet_KIUVLdHZzE4UIbVkOWXlEKN&LQGSMbqkvWvI4VCK7pI&42fRRE&c0JKrg2tGKGUS07Vdq17XjxG47_goMPbix7fAoRcfcUh2dwa0m1YQZ0FrjctYgHtF_XcDZIbwW4_bjBdjvzKGkbaQaZodoQxqeiG7cDxQvDisRsZCLEHrJncGByb0zEcCnChIzzZxzu3wveHGW2W6DuZ4D3N3pHbjBFVTaz1LvIDdQ2Dx_f_sW0SH5Pp9x8nBeWFy1YZ6TLjyHk2MkKDt0p2x06LipSQ9MRXD11IUdMYpc9pWyO&ETSG50iHrEbb9110JZOXBoNrgre2EzY3eg96aPKZnK3k2Kf_11dM3XxAM7276xFkC8kNdwISMm_x&0aes_qCtmiBK0lOntPfmVIPT4XnIkz0xSUQrbPfR549MeU1_wE6ZNlBCQcjjHqOy71T3cHKcyd7Iy1ePfjD2nAn2tm&1IdDMzn7SKT2cVuoJoMh3M2agX&dFyFEpucU3DEAjiH&o3qVz2LWXmTnfIM5Sfclk8LSyHUBiANTJXnyE_&R5G&exLPh_CjEDWXdrBSgWFc0J67PHac0IhPpvVYy_arWRxzzhWyLgLyK1yJzisQHfVRLKhmlQvnR&EWdlkD2i14w6vaZXD0wZs5f4yparUK1mITVWVfvuZvn3XLlUCj7rd3A9__22Y9pOslGfPcC1hITr4l3ydr&B0eIB9Z0iXM64w9Pyvz_GBaO02&ibspH7dfjnV2X&ZOI7mMgmush8DIR663eoaYGQab45Rj0XklisjAGr3NLUxkvDQRI8VkuMpX73N_6ninGEK8ZA001LyGudqaFdDYmqhsXBPiahcWik4mkndkyeYaHGGUfBlTKYL2XfeZNZWAt9ruK0VTCqlhcfQiR2cDBN6ALK1Salv1NO4N0yiqRbPZI0SRrLJ8FAA5KlmT2M6ydCtXuitlu8I_y140SCq3a85NG6WLMWym91sddudSr7mLnIDPUHbohRXI1tybdaofDOjtcOzdYns49sryajhhK&ofhYPBuPRc3gDc8CjsK2&l0kAWM8WyXKKkiCpq6DzeW1TRSTQHI1gGYwK7rTL2oA4aKVsowfFDAu9mt6ThQ0G0QMHXA&dY&Gn&xx9JsqEjKGWNtwWzelRdde1pavz7Fi66AHrz4zVvsIEWPWFFObTx08WcRj92yk7n1vwqFfllS&X&8iuiiavuJv8CUEsDBBQAAAAIAKWRK0ht81L9jQIAAAMIAAAfAAAAZ2l0c3luY2hpc3RhL3N5bmNfc2VsZWN0b3IucHl1ad1UUW&aMBD_KyhPnYRR7NjEqaZKBML20Ke22h66KTKJAWvGlhJntEP8951DSwm0W7VuLyMPnM535___7863m6DQoq6D8_CTkuugHwjnKjVrnATfJjBiJeHsO5zlC_Xqe1MsVe0EBDplXF5YbSsIuPqQjs7CQdj__uGAxtwb_NHzaLyDxJkovi0q25iym34S&Hy6NGKmZRmcu6qRUM1WpaxeBHJsHFaaa3kHKcEWzGrX6GYT9nvhtt&bUIr7PUqi7RYijS09H7dPbF2KmdQndM0tcFKrH1AKxydQnbxzkHrEY5vzwPP76&vayRVKrS4v&L07t&aX4QPEb2rbw&ijRKHVwqyk8U1oOXfgahoF7QUxI_M4mVKUZQwjGmGMRpOUozAkGR&RIaY47tI87PeGnmbMgPCIdFj_uu0&EX3jKXx2Nt84R29gsBRO5LVtqkLmplnNoIyd51oZDwyf6P6g2uePkFrZdb6UarEEEintlhJFIevaVvdgOWUN5NRSzwdLYUp9cHyEQMHEeKau7LqHvxj&R3oXOyPqnaljxKXU0sn8CGQXyLPXt879UDqf3j4MfppzCJWFAyr3Q8HYOB2NpxHCCUsQHROMkpiPEMv4NB5nYxxNpkfQDveHH69lTPd7SRL28sSkjXMt0NeNSzgYUsJZDFJzgilJ&vq4HHbF&MPptG&q2j8ClTX_4KWZubzxffxSjrb6DB6M4HwudC33As1aHlp1IKywlQH8lShVA3ywfUdrVbplO7YPumVTjkk6oWiSsBTRJI0QJ3GKyDgZ0QnPGHi6y0x4BEscx&uFpuF&IE8hzD&VZVf&9bpEPMziUYYRz&AEUZ5lYCUMMdAkzaLpBEe0qwsm7De6wPcTUEsDBBQAAAAIAHUCJ0i21zel2wAAALwBAAAUAAAAZ2l0c3luY2hpc3RhL3Rlc3QucHltUMtqxDAMvOsrzF5iX9x7IadS6H0&QLix7DX4ERLvoX9fO0rS3aVg0GhGGkkOaS5LFbF4CAynkl04s&UnT7hTsFAsxspWrA7M0pk_lCsAH8u3id3c0wLAUYyd0GWmjJ0J2ctWa8mJSmuV6h2EaO_5eaMY65BdkZdrNW2&3nJRTeOheDPZxm0IE&pjC19MP_6nrw2zKpXiAatJc6S94PQ4TPVCxu4iuhBJDlSnNx9qt72FtZpDZaPhP1tt72mW6vWcz2z&joHgBGI2iRDFOIoBMZmQEYf_OfxNAL9QSwMEFAAAAAgAdQInSN&tiY9BBgAAxBYAABcAAABnaXRzeW5jaGlzdGEvdWlfdXRpbC5wecVYbW&bNhD_rl&BukgjbYbR5NNgwB_yNF2DtUnhZkuBYSNkiXa4ypIgUkmDdf99x_O7LCcpOmxC0Vjk3fG5V96Jb9umk6TnCde&qmaz4fUmCd6TpGNVk5cp&M6S5MP1_dXpG&p_efb6&CNZkIm447K4oZPkx&Ornc0Vl27&w9lP784urs5e0dPLi6vl5dtQCNtsWS1ZSYumll1TKfr3b8_v6Ombk6Wi_DJJ3p18pOoQeP0hSTZVs8orRMy6JNF&YQt_zJqW1dTokgLokq1J0WzbXjIKkOhtXvUsFTKXbEqaqtQLU4IriiKbJ4TwtV4gzxZk1TRV6ijJiwEpIR2TfVd7YeQPTwIErBJsnBAX9YM4BZNohJzXrDNI3fuU1PkWgOKyBblhcJDsdqkumpplCr36oU8X_2i1xAhp2&FaksnZcnm5nCMZOTwQh6RuJFk3fV0SXhMnCPcm5ICkWqC8bwPg2YxStU5phrITp29elnTLhQBXUQWNr8BLIm1Wf7JCghi2bSuwIyoL&4qbvN4wAY5_CW&rpiOKSSGxlHBSyQtJqdYCDKQAWyotd0Dj7WKPVS9TZ1krWq9nmWHyWOyv78lR4lxsFhPrWNl0jPKabpuSValgdanMj29WO5MsaOsF0SQz9QZ7z40&AprFZBqyaBkqbP3aDKKwwyS8SaP0NHHbS17NxmIOcUXipxaQiRUMlv2nDeuBOTCNJLpszJS_oaC24jL1NcDa3FpBwVtgOCL7wkWf2tgRjsw_NxcQCTK13h3TFFMn_3oLIfFIqQkMF1UchcPDdJGFjnzIuPuK6Td4VbAKQh9KMIfXzy5NdyrXy8SH_FGSFFUuBPmVs7tTXborqAUmj2xYq&CnIBcUpWCLaj0lbd5Bwae3wLdAY899XVAUs4AA&BW8eRJUhujy5leLG165ewTAqPz862_&byTGTKJfqXW6zdsB_V3e1VCbrpvuU96pqncuRM9KoHqdg2ksalvKhqcbdbWlh5s7Su9g&00x&o4VJt4Zhb6XegaxjsZLsxAw3usaIIpQ7DuYjL16PlPkWoqndrQqVgd_88U1Xp_NGsrJnCJDBNTBx50AoYlDBzS4XDTnGqKZWhOt7vGAwCehrLijCBXDeszrHXtbBTXLrGSrfpNOxo6cmxsTK5a6NvPihql6hSCMmFCZHa8mri54W4dGfhIGWCUHQgG4LUizRq&DQnBtO7l47biCVDJRQJnIfUYi4dgxx6mTMY3UA9RDMVFv8mBEDzgdg7HZ2LZqDjDKnOt20ktXZJFm8716Is_ooun&qdxT3I0o4pbtWRxzz&dCcuXRYHDvD_TVcVBLovTiJtIGFjHLM93uLJBjPlQ_MIi&igw39piKwLeXSs7hBztOmCvp0HO5hvCh4h6SO1Mb2nFjH8&J9eXy55Pl5S8Xr_ZEfOJtC8SES9blkjfQeN7CvWi4hMq9IUjXQPvsi2A8chtddcEsEVvKW9qeHyuoEsXsYGnYT_msF7vKPiqzeB3NNOox8cueVjz0Qlw6gtOHwnaybBA&A&qdmE5MQEOzXlaM5oXylglk3RlloezH7rqwhodX3lA8Ck6GvnItljtMQWs7BgzSgNKdb9u0KqIOn3CB_ZLuBMn7ii2UIA1BdvfzJNAv5LnLoWsD0rxKs5CGfS5YK8kZ&lEBngvCBlJM5rCua7p04kmxJhV5v7mRKuAFNOH_qvFHF1UjWNyxgIE6zm4ZXXfN1k1ScU_wxwx2chgRMTEkZpx09wVuDmZFX7uA8rHpSj2PhXwKcnycm0wNQw5tYQcXO7R4fDiUegHD1B9WrxH1YbhvNEzdpGA9wAmBuIncVafoMGcOnFUGBtkzAKoHRh7Q5ci963PDltq6gytndGqQTl9Oif0ElA3tYybmyYH4clBiOwNgcALMBpQPusKKCpn2XF4jvsGPRPscRF4M0Xi1o9ptraP_&44ch5HhrvF5YPpvcDKY8t9w9CPD6JMsP5YEYybXl1M0qv6XWWHvbGKayK_wWwgg7t5GD_9r0bfqIywc5g_BCr7mn1VO7Dk4LJbqA4AvkeZT09TV0IUKu51xzw7V_NfedpYlmujGarH52CqZkKmd&mHUWAw_ENiiztV3gaBxo9CD8ppSbNi0ELign_9&kuQfUEsDBBQAAAAIAMq9Kkh8HCJUrAIAAPIFAAAcAAAAZ2l0c3luY2hpc3RhL3dvcmtpbmdfY29weS5weY1UbWvbMBD_7l9xbHRyWOqs_7ZCKGWUUcq20m70wxhCti_OF0Uykhw3hPz3nWypTrqOLYTk3nQvzz1SvW60cdBhnhvdWTQgLHR5Ug&21khZP2muXmOUV7gtlqJWUS_0slpiEnWpqyjarSo4_Rd1lSQGpRZlSu5JlA&8kyS5vby7&MyvP335enfFHy5vrr7fwhzYkYElSSV1LqQvU6FJkuGfAknIdIOKe0utqpRSFlJYCw&arMjwUTfb_7bpO0t1&gsLNzlPAOhb4gI4r1XtOE8tysXUA1OKTezOx&WRAN6dHXmp_JE_hhFW5OxFXqHjpFNbIVVfNFp9TKjCGIM7dKbGDYJbInRD&4R0s&XwgzbQGL1uHCxIFKCwA60wg3tEWDrX2PPZrKrdss2zQq9nYonKbD_czbqCe8xjmSSMNLQZF5v5nhoCjuqWKeuKezrCpsAeCyFlLooVG2aoF6B0T4ih8ZgoMCKLObiQaFzKwh7ALwJucBvSwFjZ&rPy1AcP5wy61qi_Jhys0aIqudM8oMY9amGnonC1VlNoxNbzbwqPPCbmqEQusZx&My0ervs1re&&Qe1&jhn6ZB6LeVo&nkbtlO7ajHk0&2wHUFqEflMQ2&7BaGT2MxKLlEMvmYe7m9EfqkKXmAbXJDPYSFFgyt56VE&evwsrWKyd7ylAduoho2F3Yz&73YDdfnaxC9n2Q1NUhY5Sgoy4uBYuHQ&NRzFiP3_2gnlsbYRpgC2r1UKnr66tbXvqR_TYiWWv4MSXPTjT5f3VT701mAIdOrHCtuHhftIzt0FzeNmeQbcDVqxLBufArBPGsWmg6Pihzdm2KNDaPqzZuqVWNUUP9PBUWHr1SLkI45tWvRGm2sxpDJrihSdvP74eL1M5ZGLDSOwvUPoXO7MSsUnPAlC&AVBLAQIUAxQAAAAIAJYBnUcptW2jmBoAAH9GAAAUAAAAAAAAAAAAAACkgQAAAABnaXRzeW5jaGlzdGEvTElDRU5TRVBLAQIUAxQAAAAIAEAGnUcxkLdxYQIAAG4EAAAWAAAAAAAAAAAAAACkgcoaAABnaXRzeW5jaGlzdGEvUkVBRE1FLm1kUEsBAhQDFAAAAAgAlgGdR5oAeq8QAAAADgAAACYAAAAAAAAAAAAAAKSBXx0AAGdpdHN5bmNoaXN0YS9idWlsZC9naXRzeW5jaGlzdGFfaWdub3JlUEsBAhQDFAAAAAgAlgGdRwvGKvYWAAAAFAAAACMAAAAAAAAAAAAAAKSBsx0AAGdpdHN5bmNoaXN0YS9idWlsZC9weXppcGlzdGFfaWdub3JlUEsBAhQDFAAAAAgA7QQoSIOD3lH6AwAAuQ0AABYAAAAAAAAAAAAAAKSBCh4AAGdpdHN5bmNoaXN0YS9jb25maWcucHlQSwECFAMUAAAACAClkStIJ2MsgnYAAACWAAAAJAAAAAAAAAAAAAAApIE4IgAAZ2l0c3luY2hpc3RhL2V0Yy9naXRzeW5jaGlzdGFfY29uZmlnUEsBAhQDFAAAAAgAIg0pSG8WGPQLAwAACgcAACsAAAAAAAAAAAAAAKSB8CIAAGdpdHN5bmNoaXN0YS9ldGMvZ2l0c3luY2hpc3RhX2NvbmZpZ19zYW1wbGVQSwECFAMUAAAACACWAZ1Hvk2692QAAACEAAAAIQAAAAAAAAAAAAAApIFEJgAAZ2l0c3luY2hpc3RhL2V0Yy9weXppcGlzdGFfY29uZmlnUEsBAhQDFAAAAAgAyr0qSBqCkErVAgAANggAABwAAAAAAAAAAAAAAKSB5yYAAGdpdHN5bmNoaXN0YS9naXRzeW5jaGlzdGEucHlQSwECFAMUAAAACAB1AidIwnwiowkAAAAHAAAAJAAAAAAAAAAAAAAApIH2KQAAZ2l0c3luY2hpc3RhL2xvZy9naXRzeW5jaGlzdGFfaWdub3JlUEsBAhQDFAAAAAgAZgMsSGu5PGaNAQAA3wMAABMAAAAAAAAAAAAAAKSBQSoAAGdpdHN5bmNoaXN0YS9sb2cucHlQSwECFAMUAAAACAClkStIOiPUY7EBAADYAwAAFQAAAAAAAAAAAAAApIH&KwAAZ2l0c3luY2hpc3RhL3BvcHVwLnB5UEsBAhQDFAAAAAgApZErSCI1C3QxAgAA3QUAABcAAAAAAAAAAAAAAKSB4y0AAGdpdHN5bmNoaXN0YS9wb3B1cC5weXVpUEsBAhQDFAAAAAgApZErSDDamjmADgAAiUIAABQAAAAAAAAAAAAAAKSBSTAAAGdpdHN5bmNoaXN0YS9zeW5jLnB5UEsBAhQDFAAAAAgAIg0pSBs5nu9VAQAAhAMAABsAAAAAAAAAAAAAAKSB_z4AAGdpdHN5bmNoaXN0YS9zeW5jX2NvbmZpZy5weVBLAQIUAxQAAAAIAGYDLEje9YRM8AQAAJoTAAAdAAAAAAAAAAAAAACkgYlAAABnaXRzeW5jaGlzdGEvc3luY19zZWxlY3Rvci5weVBLAQIUAxQAAAAIAKWRK0ht81L9jQIAAAMIAAAfAAAAAAAAAAAAAACkgbRFAABnaXRzeW5jaGlzdGEvc3luY19zZWxlY3Rvci5weXVpUEsBAhQDFAAAAAgAdQInSLbXN6XbAAAAvAEAABQAAAAAAAAAAAAAAKSBfkgAAGdpdHN5bmNoaXN0YS90ZXN0LnB5UEsBAhQDFAAAAAgAdQInSN&tiY9BBgAAxBYAABcAAAAAAAAAAAAAAKSBi0kAAGdpdHN5bmNoaXN0YS91aV91dGlsLnB5UEsBAhQDFAAAAAgAyr0qSHwcIlSsAgAA8gUAABwAAAAAAAAAAAAAAKSBAVAAAGdpdHN5bmNoaXN0YS93b3JraW5nX2NvcHkucHlQSwUGAAAAABQAFADCBQAA51IAAEYAR2VuZXJhdGVkIGJ5IHB5emlwaXN0YS5weSAoc2VlIGh0dHBzOi8vZ2l0aHViLmNvbS9tYXJjdXM2Ny9weXppcGlzdGEpLg==
'''

def main():

  try:  

    print "Decoding base64 encoded ZIP archive into string..."
    binary_zip_string = base64.b64decode(zip_string, '_&')
    binary_zip_input = StringIO.StringIO(binary_zip_string)
  
    print "Opening string as ZIP file..."
    zip_file = zipfile.ZipFile(binary_zip_input, "r")
  
    zip_file.printdir()
    
    print "Extracting ..."
    
    zip_file.extractall()
    
    print "All files successfully extracted into local directory."
  
  except Exception as e:
    
    sys.stderr.write("ERROR '%s' while extracting files!" % str(e))
    
if __name__ == '__main__':
  main()
  
