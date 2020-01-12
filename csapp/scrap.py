from django.shortcuts import render

import requests
import re
from bs4 import BeautifulSoup
import json
session = requests.Session()
session.headers = {"",""}

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

cat_urls =[
"https://www.amazon.in/s/ref=s9_acss_bw_cg_testref_1a1_w?i=stripbooks&bbn=1318073031&rh=n%3A976389031%2Cn%3A976390031%2Cn%3A1318073031%2Cp_n_age_range%3A1318384031%2Cp_85%3A10440599031&pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-1&pf_rd_r=M4A31705J3449VGMNBKZ&pf_rd_t=101&pf_rd_p=c676da8c-399e-45f3-ae6a-cfe381a1468c&pf_rd_i=1318073031",
"https://www.amazon.in/s/ref=s9_acss_bw_cg_testref_1b1_w?i=stripbooks&bbn=1318073031&rh=n%3A976389031%2Cn%3A976390031%2Cn%3A1318073031%2Cp_n_age_range%3A1318385031%2Cp_85%3A10440599031%2Cp_n_availability%3A1318484031&pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-1&pf_rd_r=M4A31705J3449VGMNBKZ&pf_rd_t=101&pf_rd_p=c676da8c-399e-45f3-ae6a-cfe381a1468c&pf_rd_i=1318073031",
"https://www.amazon.in/s/ref=s9_acss_bw_cg_testref_1c1_w?i=stripbooks&bbn=1318073031&rh=n%3A976389031%2Cn%3A976390031%2Cn%3A1318073031%2Cp_n_age_range%3A1318386031%2Cp_85%3A10440599031%2Cp_n_availability%3A1318484031&pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-1&pf_rd_r=M4A31705J3449VGMNBKZ&pf_rd_t=101&pf_rd_p=c676da8c-399e-45f3-ae6a-cfe381a1468c&pf_rd_i=1318073031",
"https://www.amazon.in/s/ref=s9_acss_bw_cg_testref_1d1_w?i=stripbooks&bbn=1318073031&rh=n%3A976389031%2Cn%3A976390031%2Cn%3A1318073031%2Cp_n_age_range%3A1318387031%2Cp_85%3A10440599031%2Cp_n_availability%3A1318484031&pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-1&pf_rd_r=M4A31705J3449VGMNBKZ&pf_rd_t=101&pf_rd_p=c676da8c-399e-45f3-ae6a-cfe381a1468c&pf_rd_i=1318073031",
"https://www.amazon.in/s/ref=s9_acss_bw_cg_testref_1e1_w?i=stripbooks&bbn=1318073031&rh=n%3A976389031%2Cn%3A976390031%2Cn%3A1318073031%2Cp_n_age_range%3A1318388031%2Cp_85%3A10440599031%2Cp_n_availability%3A1318484031&pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-1&pf_rd_r=M4A31705J3449VGMNBKZ&pf_rd_t=101&pf_rd_p=c676da8c-399e-45f3-ae6a-cfe381a1468c&pf_rd_i=1318073031",
"https://www.amazon.in/s/ref=s9_acss_bw_cg_spautser_1a1_w?rh=i%3Astripbooks%2Cn%3A976389031%2Cn%3A%21976390031%2Cn%3A1318073031%2Cp_85%3A10440599031%2Cp_n_availability%3A1318484031%2Cp_n_publication_date%3A2684820031&bbn=1318073031&ie=UTF8&pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-7&pf_rd_r=M4A31705J3449VGMNBKZ&pf_rd_t=101&pf_rd_p=3cd11b3a-bb10-4965-a2a1-6c269dfa93a3&pf_rd_i=1318073031",
"https://www.amazon.in/s/ref=s9_acss_bw_cg_spautser_1b1_w?rh=i%3Astripbooks%2Cn%3A976389031%2Cn%3A%21976390031%2Cn%3A1318073031%2Cp_85%3A10440599031%2Cp_n_availability%3A1318484031%2Cp_n_publication_date%3A2684821031&bbn=1318073031&ie=UTF8&pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-7&pf_rd_r=M4A31705J3449VGMNBKZ&pf_rd_t=101&pf_rd_p=3cd11b3a-bb10-4965-a2a1-6c269dfa93a3&pf_rd_i=1318073031",
"https://www.amazon.in/s/ref=s9_acss_bw_cg_spautser_1d1_w?rh=i%3Astripbooks%2Cn%3A976389031%2Cn%3A%21976390031%2Cn%3A15417300031%2Cn%3A4149807031%2Cp_n_feature_seventeen_browse-bin%3A4149849031%7C4149851031&bbn=4149807031&ie=UTF8&pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-7&pf_rd_r=M4A31705J3449VGMNBKZ&pf_rd_t=101&pf_rd_p=3cd11b3a-bb10-4965-a2a1-6c269dfa93a3&pf_rd_i=1318073031",
"https://www.amazon.in/s/ref=s9_acss_bw_cg_spautser_3a1_w?rh=i%3Astripbooks%2Cn%3A976389031%2Cn%3A1318073031%2Ck%3ADavid+walliams%2Cp_85%3A10440599031&ie=UTF8&pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-7&pf_rd_r=M4A31705J3449VGMNBKZ&pf_rd_t=101&pf_rd_p=3cd11b3a-bb10-4965-a2a1-6c269dfa93a3&pf_rd_i=1318073031",
"https://www.amazon.in/s/ref=s9_acss_bw_cg_spautser_3b1_w?rh=i%3Astripbooks%2Cn%3A976389031%2Ck%3Adr.seuss+books+for+children%2Cp_n_availability%3A1318484031%2Cp_lbr_books_authors_browse-bin%3ADr.+Seuss%2Cp_85%3A10440599031&ie=UTF8&pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-7&pf_rd_r=M4A31705J3449VGMNBKZ&pf_rd_t=101&pf_rd_p=3cd11b3a-bb10-4965-a2a1-6c269dfa93a3&pf_rd_i=1318073031",
"https://www.amazon.in/s/ref=s9_acss_bw_cg_spautser_3c1_w?rh=i%3Astripbooks%2Cn%3A976389031%2Cn%3A1318073031%2Ck%3AEnid+Blyton%2Cp_85%3A10440599031%2Cp_n_availability%3A1318484031&ie=UTF8&pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-7&pf_rd_r=M4A31705J3449VGMNBKZ&pf_rd_t=101&pf_rd_p=3cd11b3a-bb10-4965-a2a1-6c269dfa93a3&pf_rd_i=1318073031",
"https://www.amazon.in/s/ref=s9_acss_bw_cg_spautser_3d1_w?rh=i%3Astripbooks%2Cn%3A976389031%2Cn%3A1318073031%2Ck%3Aj.k.+rowling%2Cp_85%3A10440599031%2Cp_n_availability%3A1318484031&ie=UTF8&pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-7&pf_rd_r=M4A31705J3449VGMNBKZ&pf_rd_t=101&pf_rd_p=3cd11b3a-bb10-4965-a2a1-6c269dfa93a3&pf_rd_i=1318073031",
"https://www.amazon.in/s/ref=s9_acss_bw_cg_spautser_3e1_w?rh=i%3Astripbooks%2Cn%3A976389031%2Cn%3A1318073031%2Ck%3AJohn+Green%2Cp_85%3A10440599031%2Cp_n_availability%3A1318484031&ie=UTF8&pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-7&pf_rd_r=M4A31705J3449VGMNBKZ&pf_rd_t=101&pf_rd_p=3cd11b3a-bb10-4965-a2a1-6c269dfa93a3&pf_rd_i=1318073031",
"https://www.amazon.in/s/ref=s9_acss_bw_cg_spautser_3f1_w?rh=i%3Astripbooks%2Cn%3A976389031%2Cn%3A1318073031%2Ck%3AMark+twain%2Cp_85%3A10440599031%2Cp_n_availability%3A1318484031&ie=UTF8&pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-7&pf_rd_r=M4A31705J3449VGMNBKZ&pf_rd_t=101&pf_rd_p=3cd11b3a-bb10-4965-a2a1-6c269dfa93a3&pf_rd_i=1318073031",
"https://www.amazon.in/s/ref=s9_acss_bw_cg_spautser_4a1_w?rh=i%3Astripbooks%2Cn%3A976389031%2Cn%3A1318073031%2Ck%3ARick+riordan%2Cp_85%3A10440599031%2Cp_n_availability%3A1318484031&ie=UTF8&pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-7&pf_rd_r=M4A31705J3449VGMNBKZ&pf_rd_t=101&pf_rd_p=3cd11b3a-bb10-4965-a2a1-6c269dfa93a3&pf_rd_i=1318073031",
"https://www.amazon.in/s/ref=s9_acss_bw_cg_spautser_4b1_w?rh=i%3Astripbooks%2Cn%3A976389031%2Cn%3A1318073031%2Ck%3ARoald+Dahl%2Cp_85%3A10440599031%2Cp_n_availability%3A1318484031&ie=UTF8&pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-7&pf_rd_r=M4A31705J3449VGMNBKZ&pf_rd_t=101&pf_rd_p=3cd11b3a-bb10-4965-a2a1-6c269dfa93a3&pf_rd_i=1318073031",
"https://www.amazon.in/s/ref=s9_acss_bw_cg_spautser_4c1_w?rh=i%3Astripbooks%2Cn%3A976389031%2Cn%3A1318073031%2Ck%3ARobert+louis+stevenson%2Cp_85%3A10440599031%2Cp_n_availability%3A1318484031&ie=UTF8&pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-7&pf_rd_r=M4A31705J3449VGMNBKZ&pf_rd_t=101&pf_rd_p=3cd11b3a-bb10-4965-a2a1-6c269dfa93a3&pf_rd_i=1318073031",
"https://www.amazon.in/s/ref=s9_acss_bw_cg_spautser_4d1_w?rh=i%3Astripbooks%2Cn%3A976389031%2Cn%3A1318073031%2Ck%3ARudyard+kipling%2Cp_85%3A10440599031%2Cp_n_availability%3A1318484031&ie=UTF8&pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-7&pf_rd_r=M4A31705J3449VGMNBKZ&pf_rd_t=101&pf_rd_p=3cd11b3a-bb10-4965-a2a1-6c269dfa93a3&pf_rd_i=1318073031",
"https://www.amazon.in/s/ref=s9_acss_bw_cg_spautser_4e1_w?rh=i%3Astripbooks%2Cn%3A976389031%2Cn%3A1318073031%2Ck%3ARuskin+bond%2Cp_85%3A10440599031%2Cp_n_availability%3A1318484031&ie=UTF8&pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-7&pf_rd_r=M4A31705J3449VGMNBKZ&pf_rd_t=101&pf_rd_p=3cd11b3a-bb10-4965-a2a1-6c269dfa93a3&pf_rd_i=1318073031",
"https://www.amazon.in/s/ref=s9_acss_bw_cg_spautser_4f1_w?rh=i%3Astripbooks%2Cn%3A976389031%2Cn%3A1318073031%2Ck%3ASudha+murty%2Cp_85%3A10440599031%2Cp_n_availability%3A1318484031&ie=UTF8&pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-7&pf_rd_r=M4A31705J3449VGMNBKZ&pf_rd_t=101&pf_rd_p=3cd11b3a-bb10-4965-a2a1-6c269dfa93a3&pf_rd_i=1318073031",
"https://www.amazon.in/s/ref=s9_acss_bw_cg_spautser_6b1_w?rh=i%3Astripbooks%2Cn%3A976389031%2Ck%3AEnid+Blyton%2Cp_85%3A10440599031%2Cp_n_binding_browse-bin%3A1318376031%2Cp_n_availability%3A1318484031%2Cp_lbr_books_authors_browse-bin%3AEnid+Blyton&ie=UTF8&pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-7&pf_rd_r=M4A31705J3449VGMNBKZ&pf_rd_t=101&pf_rd_p=3cd11b3a-bb10-4965-a2a1-6c269dfa93a3&pf_rd_i=1318073031",
"https://www.amazon.in/s/ref=s9_acss_bw_cg_spautser_6d1_w?rh=i%3Astripbooks%2Cn%3A976389031%2Ck%3AVeronica+Roth%2Cp_85%3A10440599031%2Cp_lbr_books_authors_browse-bin%3AVeronica+Roth%2Cp_n_availability%3A1318484031&ie=UTF8&pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-7&pf_rd_r=M4A31705J3449VGMNBKZ&pf_rd_t=101&pf_rd_p=3cd11b3a-bb10-4965-a2a1-6c269dfa93a3&pf_rd_i=1318073031",
"https://www.amazon.in/s/ref=s9_acss_bw_cg_spautser_6e1_w?rh=i%3Astripbooks%2Cn%3A976389031%2Ck%3ARachel+Renee+Russell%2Cp_85%3A10440599031%2Cp_n_availability%3A1318484031&ie=UTF8&pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-7&pf_rd_r=M4A31705J3449VGMNBKZ&pf_rd_t=101&pf_rd_p=3cd11b3a-bb10-4965-a2a1-6c269dfa93a3&pf_rd_i=1318073031",
"https://www.amazon.in/s/ref=s9_acss_bw_cg_spautser_6f1_w?rh=i%3Astripbooks%2Cn%3A976389031%2Ck%3ASuzanne+Collins%2Cp_85%3A10440599031%2Cp_n_availability%3A1318484031&ie=UTF8&pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-7&pf_rd_r=M4A31705J3449VGMNBKZ&pf_rd_t=101&pf_rd_p=3cd11b3a-bb10-4965-a2a1-6c269dfa93a3&pf_rd_i=1318073031",
"https://www.amazon.in/s/ref=s9_acss_bw_cg_spautser_7b1_w?rh=i%3Astripbooks%2Cn%3A976389031%2Ck%3AJames+Dashner%2Cp_85%3A10440599031%2Cp_n_availability%3A1318484031&ie=UTF8&pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-7&pf_rd_r=M4A31705J3449VGMNBKZ&pf_rd_t=101&pf_rd_p=3cd11b3a-bb10-4965-a2a1-6c269dfa93a3&pf_rd_i=1318073031",
"https://www.amazon.in/s/ref=s9_acss_bw_cg_spautser_7c1_w?rh=i%3Astripbooks%2Cn%3A976389031%2Ck%3ALemony+Snicket%2Cp_85%3A10440599031%2Cp_lbr_books_authors_browse-bin%3ALemony+Snicket%2Cp_n_availability%3A1318484031&ie=UTF8&pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-7&pf_rd_r=M4A31705J3449VGMNBKZ&pf_rd_t=101&pf_rd_p=3cd11b3a-bb10-4965-a2a1-6c269dfa93a3&pf_rd_i=1318073031",
"https://www.amazon.in/s/ref=s9_acss_bw_cg_spautser_7d1_w?rh=i%3Astripbooks%2Cn%3A976389031%2Ck%3AC.S.+Lewis%2Cp_85%3A10440599031%2Cp_n_availability%3A1318484031%2Cp_lbr_books_authors_browse-bin%3AC.S.+Lewis&ie=UTF8&pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-7&pf_rd_r=M4A31705J3449VGMNBKZ&pf_rd_t=101&pf_rd_p=3cd11b3a-bb10-4965-a2a1-6c269dfa93a3&pf_rd_i=1318073031",
"https://www.amazon.in/s/ref=s9_acss_bw_cg_spautser_7e1_w?rh=i%3Astripbooks%2Cn%3A976389031%2Ck%3Anancy+drew+books%2Cp_85%3A10440599031%2Cp_n_availability%3A1318484031&ie=UTF8&pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-7&pf_rd_r=M4A31705J3449VGMNBKZ&pf_rd_t=101&pf_rd_p=3cd11b3a-bb10-4965-a2a1-6c269dfa93a3&pf_rd_i=1318073031",
"https://www.amazon.in/s/ref=s9_acss_bw_cg_spautser_7f1_w?rh=i%3Astripbooks%2Cn%3A976389031%2Ck%3Athe+hardy+boys%2Cp_85%3A10440599031%2Cp_n_availability%3A1318484031&ie=UTF8&pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-7&pf_rd_r=M4A31705J3449VGMNBKZ&pf_rd_t=101&pf_rd_p=3cd11b3a-bb10-4965-a2a1-6c269dfa93a3&pf_rd_i=1318073031",
"https://www.amazon.in/s/ref=s9_acss_bw_cg_spautser_8a1_w?rh=i%3Astripbooks%2Cn%3A976389031%2Ck%3AStephenie+Meyer%2Cp_85%3A10440599031%2Cp_n_availability%3A1318484031&ie=UTF8&pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-7&pf_rd_r=M4A31705J3449VGMNBKZ&pf_rd_t=101&pf_rd_p=3cd11b3a-bb10-4965-a2a1-6c269dfa93a3&pf_rd_i=1318073031",
"https://www.amazon.in/s/ref=s9_acss_bw_cg_spautser_8b1_w?rh=i%3Astripbooks%2Cn%3A976389031%2Ck%3Athe+lord+of+the+rings%2Cp_85%3A10440599031%2Cp_n_feature_three_browse-bin%3A9141482031%2Cp_n_availability%3A1318484031&ie=UTF8&pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-7&pf_rd_r=M4A31705J3449VGMNBKZ&pf_rd_t=101&pf_rd_p=3cd11b3a-bb10-4965-a2a1-6c269dfa93a3&pf_rd_i=1318073031",
"https://www.amazon.in/s/ref=s9_acss_bw_cg_spautser_8c1_w?rh=i%3Astripbooks%2Cn%3A976389031%2Ck%3Aasterix%2Cp_85%3A10440599031%2Cp_n_feature_three_browse-bin%3A9141482031%2Cp_n_availability%3A1318484031&ie=UTF8&pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-7&pf_rd_r=M4A31705J3449VGMNBKZ&pf_rd_t=101&pf_rd_p=3cd11b3a-bb10-4965-a2a1-6c269dfa93a3&pf_rd_i=1318073031",
"https://www.amazon.in/s/ref=s9_acss_bw_cg_spautser_8d1_w?rh=i%3Astripbooks%2Cn%3A976389031%2Ck%3AChristopher+Paolini%2Cp_85%3A10440599031%2Cp_n_availability%3A1318484031&ie=UTF8&pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-7&pf_rd_r=M4A31705J3449VGMNBKZ&pf_rd_t=101&pf_rd_p=3cd11b3a-bb10-4965-a2a1-6c269dfa93a3&pf_rd_i=1318073031",
"https://www.amazon.in/s/ref=s9_acss_bw_cg_spautser_8e1_w?rh=i%3Astripbooks%2Cn%3A976389031%2Ck%3Aadventure+of+tintin%2Cp_85%3A10440599031%2Cp_n_availability%3A1318484031%2Cp_n_feature_three_browse-bin%3A9141482031&ie=UTF8&pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-7&pf_rd_r=M4A31705J3449VGMNBKZ&pf_rd_t=101&pf_rd_p=3cd11b3a-bb10-4965-a2a1-6c269dfa93a3&pf_rd_i=1318073031",
"https://www.amazon.in/s/ref=s9_acss_bw_cg_spautser_8f1_w?rh=i%3Astripbooks%2Cn%3A976389031%2Ck%3Athe+mortal+instruments%2Cp_85%3A10440599031%2Cp_n_availability%3A1318484031&ie=UTF8&pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-7&pf_rd_r=M4A31705J3449VGMNBKZ&pf_rd_t=101&pf_rd_p=3cd11b3a-bb10-4965-a2a1-6c269dfa93a3&pf_rd_i=1318073031",
"https://www.amazon.in/s/ref=s9_acss_bw_cg_spautser_11a1_w?rh=i%3Astripbooks%2Cn%3A976389031%2Cn%3A%211318447031%2Cn%3A%211318449031%2Cn%3A3605992031%2Cn%3A1318073031%2Cp_85%3A10440599031%2Cp_n_availability%3A1318484031&bbn=3605992031&ie=UTF8&pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-7&pf_rd_r=M4A31705J3449VGMNBKZ&pf_rd_t=101&pf_rd_p=3cd11b3a-bb10-4965-a2a1-6c269dfa93a3&pf_rd_i=1318073031",
"https://www.amazon.in/s/ref=lp_1318073031_hi_1/257-6349273-2010341?rh=n%3A976389031&ie=UTF8&qid=1578753667",
"https://www.amazon.in/s/ref=lp_1318073031_il_ti_stripbooks/257-6349273-2010341?rh=n%3A976389031%2Cn%3A%21976390031%2Cn%3A1318073031&ie=UTF8&qid=1578753667&lo=stripbooks",
"https://www.amazon.in/s/ref=lp_1318073031_pg_2/257-6349273-2010341?rh=n%3A976389031%2Cn%3A%21976390031%2Cn%3A1318073031&page=2&ie=UTF8&qid=1578753667",
"https://www.amazon.in/s/ref=lp_1318073031_pg_3/257-6349273-2010341?rh=n%3A976389031%2Cn%3A%21976390031%2Cn%3A1318073031&page=3&ie=UTF8&qid=1578753667",
"https://www.amazon.in/s/ref=lp_1318073031_pg_2/257-6349273-2010341?rh=n%3A976389031%2Cn%3A%21976390031%2Cn%3A1318073031&page=2&ie=UTF8&qid=1578753667",
"https://www.amazon.in/s/ref=lp_1318073031_ex_n_1/257-6349273-2010341?rh=n%3A976389031&bbn=976389031&ie=UTF8&qid=1578753667",
"https://www.amazon.in/s/ref=lp_1318073031_nr_n_0/257-6349273-2010341?fst=as%3Aoff&rh=n%3A976389031%2Cn%3A%21976390031%2Cn%3A1318073031%2Cn%3A1318084031&bbn=1318073031&ie=UTF8&qid=1578753667&rnid=1318073031",
"https://www.amazon.in/s/ref=lp_1318073031_nr_n_1/257-6349273-2010341?fst=as%3Aoff&rh=n%3A976389031%2Cn%3A%21976390031%2Cn%3A1318073031%2Cn%3A1318074031&bbn=1318073031&ie=UTF8&qid=1578753667&rnid=1318073031",
"https://www.amazon.in/s/ref=lp_1318073031_nr_n_2/257-6349273-2010341?fst=as%3Aoff&rh=n%3A976389031%2Cn%3A%21976390031%2Cn%3A1318073031%2Cn%3A1318075031&bbn=1318073031&ie=UTF8&qid=1578753667&rnid=1318073031",
"https://www.amazon.in/s/ref=lp_1318073031_nr_n_3/257-6349273-2010341?fst=as%3Aoff&rh=n%3A976389031%2Cn%3A%21976390031%2Cn%3A1318073031%2Cn%3A1318086031&bbn=1318073031&ie=UTF8&qid=1578753667&rnid=1318073031",
"https://www.amazon.in/s/ref=lp_1318073031_nr_n_4/257-6349273-2010341?fst=as%3Aoff&rh=n%3A976389031%2Cn%3A%21976390031%2Cn%3A1318073031%2Cn%3A1318076031&bbn=1318073031&ie=UTF8&qid=1578753667&rnid=1318073031",
"https://www.amazon.in/s/ref=lp_1318073031_nr_n_5/257-6349273-2010341?fst=as%3Aoff&rh=n%3A976389031%2Cn%3A%21976390031%2Cn%3A1318073031%2Cn%3A1318077031&bbn=1318073031&ie=UTF8&qid=1578753667&rnid=1318073031",
"https://www.amazon.in/s/ref=lp_1318073031_nr_n_6/257-6349273-2010341?fst=as%3Aoff&rh=n%3A976389031%2Cn%3A%21976390031%2Cn%3A1318073031%2Cn%3A1402037031&bbn=1318073031&ie=UTF8&qid=1578753667&rnid=1318073031",
"https://www.amazon.in/s/ref=lp_1318073031_nr_n_7/257-6349273-2010341?fst=as%3Aoff&rh=n%3A976389031%2Cn%3A%21976390031%2Cn%3A1318073031%2Cn%3A1318078031&bbn=1318073031&ie=UTF8&qid=1578753667&rnid=1318073031",
"https://www.amazon.in/s/ref=lp_1318073031_nr_n_8/257-6349273-2010341?fst=as%3Aoff&rh=n%3A976389031%2Cn%3A%21976390031%2Cn%3A1318073031%2Cn%3A1318088031&bbn=1318073031&ie=UTF8&qid=1578753667&rnid=1318073031",
"https://www.amazon.in/s/ref=lp_1318073031_nr_n_9/257-6349273-2010341?fst=as%3Aoff&rh=n%3A976389031%2Cn%3A%21976390031%2Cn%3A1318073031%2Cn%3A1318079031&bbn=1318073031&ie=UTF8&qid=1578753667&rnid=1318073031",
"https://www.amazon.in/s/ref=lp_1318073031_nr_n_10/257-6349273-2010341?fst=as%3Aoff&rh=n%3A976389031%2Cn%3A%21976390031%2Cn%3A1318073031%2Cn%3A1318080031&bbn=1318073031&ie=UTF8&qid=1578753667&rnid=1318073031",
"https://www.amazon.in/s/ref=lp_1318073031_nr_n_11/257-6349273-2010341?fst=as%3Aoff&rh=n%3A976389031%2Cn%3A%21976390031%2Cn%3A1318073031%2Cn%3A1318081031&bbn=1318073031&ie=UTF8&qid=1578753667&rnid=1318073031",
"https://www.amazon.in/s/ref=lp_1318073031_nr_n_12/257-6349273-2010341?fst=as%3Aoff&rh=n%3A976389031%2Cn%3A%21976390031%2Cn%3A1318073031%2Cn%3A1318082031&bbn=1318073031&ie=UTF8&qid=1578753667&rnid=1318073031",
"https://www.amazon.in/s/ref=lp_1318073031_nr_n_13/257-6349273-2010341?fst=as%3Aoff&rh=n%3A976389031%2Cn%3A%21976390031%2Cn%3A1318073031%2Cn%3A1318083031&bbn=1318073031&ie=UTF8&qid=1578753667&rnid=1318073031",
"https://www.amazon.in/s/ref=lp_1318073031_nr_n_14/257-6349273-2010341?fst=as%3Aoff&rh=n%3A976389031%2Cn%3A%21976390031%2Cn%3A1318073031%2Cn%3A1318096031&bbn=1318073031&ie=UTF8&qid=1578753667&rnid=1318073031",
"https://www.amazon.in/s/ref=lp_1318073031_nr_n_15/257-6349273-2010341?fst=as%3Aoff&rh=n%3A976389031%2Cn%3A%21976390031%2Cn%3A1318073031%2Cn%3A1318097031&bbn=1318073031&ie=UTF8&qid=1578753667&rnid=1318073031",
"https://www.amazon.in/s/ref=lp_1318073031_nr_n_16/257-6349273-2010341?fst=as%3Aoff&rh=n%3A976389031%2Cn%3A%21976390031%2Cn%3A1318073031%2Cn%3A1318098031&bbn=1318073031&ie=UTF8&qid=1578753667&rnid=1318073031",
"https://www.amazon.in/s/ref=lp_1318073031_nr_n_17/257-6349273-2010341?fst=as%3Aoff&rh=n%3A976389031%2Cn%3A%21976390031%2Cn%3A1318073031%2Cn%3A1318099031&bbn=1318073031&ie=UTF8&qid=1578753667&rnid=1318073031",
"https://www.amazon.in/s/ref=lp_1318073031_nr_n_18/257-6349273-2010341?fst=as%3Aoff&rh=n%3A976389031%2Cn%3A%21976390031%2Cn%3A1318073031%2Cn%3A1318100031&bbn=1318073031&ie=UTF8&qid=1578753667&rnid=1318073031",
"https://www.amazon.in/s/ref=lp_1318073031_nr_n_19/257-6349273-2010341?fst=as%3Aoff&rh=n%3A976389031%2Cn%3A%21976390031%2Cn%3A1318073031%2Cn%3A1318101031&bbn=1318073031&ie=UTF8&qid=1578753667&rnid=1318073031",
"https://www.amazon.in/s/ref=lp_1318073031_nr_n_20/257-6349273-2010341?fst=as%3Aoff&rh=n%3A976389031%2Cn%3A%21976390031%2Cn%3A1318073031%2Cn%3A1318102031&bbn=1318073031&ie=UTF8&qid=1578753667&rnid=1318073031",
"https://www.amazon.in/s/ref=lp_1318073031_nr_n_21/257-6349273-2010341?fst=as%3Aoff&rh=n%3A976389031%2Cn%3A%21976390031%2Cn%3A1318073031%2Cn%3A1318103031&bbn=1318073031&ie=UTF8&qid=1578753667&rnid=1318073031",
"https://www.amazon.in/s/ref=lp_1318073031_nr_n_22/257-6349273-2010341?fst=as%3Aoff&rh=n%3A976389031%2Cn%3A%21976390031%2Cn%3A1318073031%2Cn%3A1318092031&bbn=1318073031&ie=UTF8&qid=1578753667&rnid=1318073031",
"https://www.amazon.in/s/ref=lp_1318073031_nr_p_n_publication_date_0/257-6349273-2010341?fst=as%3Aoff&rh=n%3A976389031%2Cn%3A%21976390031%2Cn%3A1318073031%2Cp_n_publication_date%3A2684819031&bbn=1318073031&ie=UTF8&qid=1578753667&rnid=2684818031",
"https://www.amazon.in/s/ref=lp_1318073031_nr_p_n_publication_date_1/257-6349273-2010341?fst=as%3Aoff&rh=n%3A976389031%2Cn%3A%21976390031%2Cn%3A1318073031%2Cp_n_publication_date%3A2684820031&bbn=1318073031&ie=UTF8&qid=1578753667&rnid=2684818031",
"https://www.amazon.in/s/ref=lp_1318073031_nr_p_n_publication_date_2/257-6349273-2010341?fst=as%3Aoff&rh=n%3A976389031%2Cn%3A%21976390031%2Cn%3A1318073031%2Cp_n_publication_date%3A2684821031&bbn=1318073031&ie=UTF8&qid=1578753667&rnid=2684818031",
"https://www.amazon.in/s/ref=lp_1318073031_nr_p_n_age_range_0/257-6349273-2010341?fst=as%3Aoff&rh=n%3A976389031%2Cn%3A%21976390031%2Cn%3A1318073031%2Cp_n_age_range%3A1318384031&bbn=1318073031&ie=UTF8&qid=1578753667&rnid=1318383031",
"https://www.amazon.in/s/ref=lp_1318073031_nr_p_n_age_range_1/257-6349273-2010341?fst=as%3Aoff&rh=n%3A976389031%2Cn%3A%21976390031%2Cn%3A1318073031%2Cp_n_age_range%3A1318385031&bbn=1318073031&ie=UTF8&qid=1578753667&rnid=1318383031",
"https://www.amazon.in/s/ref=lp_1318073031_nr_p_n_age_range_2/257-6349273-2010341?fst=as%3Aoff&rh=n%3A976389031%2Cn%3A%21976390031%2Cn%3A1318073031%2Cp_n_age_range%3A1318386031&bbn=1318073031&ie=UTF8&qid=1578753667&rnid=1318383031",
"https://www.amazon.in/s/ref=lp_1318073031_nr_p_n_age_range_3/257-6349273-2010341?fst=as%3Aoff&rh=n%3A976389031%2Cn%3A%21976390031%2Cn%3A1318073031%2Cp_n_age_range%3A1318387031&bbn=1318073031&ie=UTF8&qid=1578753667&rnid=1318383031",
"https://www.amazon.in/s/ref=lp_1318073031_nr_p_n_age_range_4/257-6349273-2010341?fst=as%3Aoff&rh=n%3A976389031%2Cn%3A%21976390031%2Cn%3A1318073031%2Cp_n_age_range%3A1318388031&bbn=1318073031&ie=UTF8&qid=1578753667&rnid=1318383031",
"https://www.amazon.in/s/ref=lp_1318073031_nr_p_72_0/257-6349273-2010341?fst=as%3Aoff&rh=n%3A976389031%2Cn%3A%21976390031%2Cn%3A1318073031%2Cp_72%3A1318476031&bbn=1318073031&ie=UTF8&qid=1578753667&rnid=1318475031",
"https://www.amazon.in/s/ref=lp_1318073031_nr_p_72_1/257-6349273-2010341?fst=as%3Aoff&rh=n%3A976389031%2Cn%3A%21976390031%2Cn%3A1318073031%2Cp_72%3A1318477031&bbn=1318073031&ie=UTF8&qid=1578753667&rnid=1318475031",
"https://www.amazon.in/s/ref=lp_1318073031_nr_p_72_2/257-6349273-2010341?fst=as%3Aoff&rh=n%3A976389031%2Cn%3A%21976390031%2Cn%3A1318073031%2Cp_72%3A1318478031&bbn=1318073031&ie=UTF8&qid=1578753667&rnid=1318475031",
"https://www.amazon.in/s/ref=lp_1318073031_nr_p_72_3/257-6349273-2010341?fst=as%3Aoff&rh=n%3A976389031%2Cn%3A%21976390031%2Cn%3A1318073031%2Cp_72%3A1318479031&bbn=1318073031&ie=UTF8&qid=1578753667&rnid=1318475031",
"https://www.amazon.in/s/ref=lp_1318073031_nr_p_n_condition-type_0/257-6349273-2010341?fst=as%3Aoff&rh=n%3A976389031%2Cn%3A%21976390031%2Cn%3A1318073031%2Cp_n_condition-type%3A8609960031&bbn=1318073031&ie=UTF8&qid=1578753667&rnid=8609959031",
"https://www.amazon.in/s/ref=lp_1318073031_nr_p_n_condition-type_1/257-6349273-2010341?fst=as%3Aoff&rh=n%3A976389031%2Cn%3A%21976390031%2Cn%3A1318073031%2Cp_n_condition-type%3A8609962031&bbn=1318073031&ie=UTF8&qid=1578753667&rnid=8609959031",
"https://www.amazon.in/s/ref=lp_1318073031_nr_p_36_0/257-6349273-2010341?fst=as%3Aoff&rh=n%3A976389031%2Cn%3A%21976390031%2Cn%3A1318073031%2Cp_36%3A1741388031&bbn=1318073031&ie=UTF8&qid=1578753667&rnid=1741387031",
"https://www.amazon.in/s/ref=lp_1318073031_nr_p_36_1/257-6349273-2010341?fst=as%3Aoff&rh=n%3A976389031%2Cn%3A%21976390031%2Cn%3A1318073031%2Cp_36%3A1741389031&bbn=1318073031&ie=UTF8&qid=1578753667&rnid=1741387031",
"https://www.amazon.in/s/ref=lp_1318073031_nr_p_36_2/257-6349273-2010341?fst=as%3Aoff&rh=n%3A976389031%2Cn%3A%21976390031%2Cn%3A1318073031%2Cp_36%3A1741390031&bbn=1318073031&ie=UTF8&qid=1578753667&rnid=1741387031",
"https://www.amazon.in/s/ref=lp_1318073031_nr_p_36_3/257-6349273-2010341?fst=as%3Aoff&rh=n%3A976389031%2Cn%3A%21976390031%2Cn%3A1318073031%2Cp_36%3A1741391031&bbn=1318073031&ie=UTF8&qid=1578753667&rnid=1741387031",
"https://www.amazon.in/s/ref=lp_1318073031_nr_p_36_4/257-6349273-2010341?fst=as%3Aoff&rh=n%3A976389031%2Cn%3A%21976390031%2Cn%3A1318073031%2Cp_36%3A1741392031&bbn=1318073031&ie=UTF8&qid=1578753667&rnid=1741387031",
"https://www.amazon.in/s/ref=lp_1318073031_nr_p_n_pct-off-with-tax_0/257-6349273-2010341?fst=as%3Aoff&rh=n%3A976389031%2Cn%3A%21976390031%2Cn%3A1318073031%2Cp_n_pct-off-with-tax%3A2665399031&bbn=1318073031&ie=UTF8&qid=1578753667&rnid=2665398031",
"https://www.amazon.in/s/ref=lp_1318073031_nr_p_n_pct-off-with-tax_1/257-6349273-2010341?fst=as%3Aoff&rh=n%3A976389031%2Cn%3A%21976390031%2Cn%3A1318073031%2Cp_n_pct-off-with-tax%3A2665400031&bbn=1318073031&ie=UTF8&qid=1578753667&rnid=2665398031",
"https://www.amazon.in/s/ref=lp_1318073031_nr_p_n_pct-off-with-tax_2/257-6349273-2010341?fst=as%3Aoff&rh=n%3A976389031%2Cn%3A%21976390031%2Cn%3A1318073031%2Cp_n_pct-off-with-tax%3A2665402031&bbn=1318073031&ie=UTF8&qid=1578753667&rnid=2665398031",
"https://www.amazon.in/s/ref=lp_1318073031_nr_p_n_pct-off-with-tax_3/257-6349273-2010341?fst=as%3Aoff&rh=n%3A976389031%2Cn%3A%21976390031%2Cn%3A1318073031%2Cp_n_pct-off-with-tax%3A2665401031&bbn=1318073031&ie=UTF8&qid=1578753667&rnid=2665398031"]

list_of_error_proxy=[]
current_proxy=''
def get_con(url,proxy):
    try:
        return session.get(url).content
    except:
        print('Error Reconnecting 2:',proxy)
        return 'error'
    
def books_all_scrap():
    book_list_all=[]
    pi = 0
    pi2 =0
    for url_ct in cat_urls:
        book_list_all_2=[]
        pi2=pi2+1
        proxy2 = ''
        print proxy2
        iop = 0
        for x in range(0,75):
            iop = iop +1
            if iop>20:
                iop = 0
                proxy2 = ''
                print proxy2
                
            url = url_ct+"&page="+str(x)
            content = get_con(url,proxy2)
            # print("got this content:",content)
            if(content!='error'):
                print('connected:',proxy2)
                
            while(content=='error') :
                print('Error Reconnecting:',proxy2)
                proxy2 =list_proxies()
                content=get_con(url,proxy2)

            soup = BeautifulSoup(content, "html5lib")
            book_list_temp = soup.findAll('a',{'class':'a-link-normal a-text-normal'})
            title = soup.find('title')
            title=title.text
            title=title.replace('<title>','')
            title= title.replace('</title>','')
            title= title.replace('/','')
            title= title.replace('\n','')
            title= title.replace('.com','')
            title= title.replace(':','_')
            title= title.replace('.','')
            title= title.replace(' ','_')
            title= title.replace('"','_')
            print ("for page ",x," --",title)
            if len(book_list_temp) ==0:
                print ("errored for", title)
            for book in book_list_temp:
                
                book_i = books_all_scrap_one("https://www.amazon.in"+book.get('href'))

                if(check_if_redacted(book_i[0])=='no'):
                    pi =pi +1
                    book_list_all_2.append(book_i)
                    book_list_all.append(book_i)
                    print("Currently scraping Page: ",x,"  of category ",title," Total Books scrapped: ",pi,"Working....",book_i[0] )

        f= open("/home/user88/Desktop/Iwyno/scrap_outputs/"+str(pi2)+"_"+title+".json","w+")
        f.write(json.dumps(book_list_all_2))
        f.close() 
    
    f= open("/home/user88/Desktop/Iwyno/scrap_outputs/all.json","w+")
    f.write(json.dumps(book_list_all))
    f.close() 
    return book_list_all 

def books_all_scrap_one(turl):

    url = turl
    book_list_all=[]
    content = session.get(url, verify=False).content
    x = re.search("/dp/+", url)

    if (x):
        print('received :',url)
        try:
            soup = BeautifulSoup(content, "html5lib")
            name = soup.find('span',{'class':'a-size-large'}).text
            try:
                image_url = soup.find('img',{'id':'imgBlkFront'}).get('data-a-dynamic-image')
            except :
                image_url = soup.find('img',{'id':'ebooksImgBlkFront'}).get('data-a-dynamic-image')

            book_list_all.append("Book Name: " +name)
            book_list_all.append("Image_url: "+image_url)

            cc = soup.find('div',{'class':'content'})
            t2 = cc.findAll('li')

            for x in range(len(t2)):
                book_list_all.append(t2[x].text)
            
            ccs =  soup.select('noscript')[1].get_text(strip=True)
            book_list_all.append("Desc: "+ccs)
            print ("name :", name)

        except :
            print('upped redacted')
            book_list_all.append("REDACTED")

        return book_list_all 

    else:
        print('bottom redacted')
        return 'REDACTED ADVERTISEMENT-ERROR: '

def is_it_a_book_or_category(url):

    x = re.search("/dp/+", url)
    y = re.search("/s/+", url)
    if x:
        return 'book'
    elif y:
        return 'category'

def check_if_redacted(url):

    x = re.search("REDACTED", url[0])

    if (x or url=='R' or url=='REDACTED'):
        return 'yes'
    else:
        return 'no'


def list_proxies():
    working_proxy_list =[]
    url = 'https://free-proxy-list.net/'

    content = session.get(url, verify=False).content

    soup = BeautifulSoup(content, "html5lib")
    oo =   soup.find('table',{"id":"proxylisttable"})
    ooo = oo.findAll('tr')
    i =0
    for o4 in ooo:
        try:
            ooi = str(o4.findAll('td')[0].contents[0])
            ooi2=str(o4.findAll('td')[1].contents[0])
            ooi3=str(o4.findAll('td')[1].contents[0])
            ooi3=str(o4.findAll('td')[6].contents[0])
            if(ooi3=='yes'):
                
                built = ooi+":"+ooi2
                print("is yes", built)
                if(check_the_proxy_connection(built)=='connected'):
                    return built                
        except:
            print ''
    return working_proxy_list

def check_the_proxy_connection(p):
    global list_of_error_proxy,current_proxy
    if(p in list_of_error_proxy):
        return 'error'
        
    url = 'https://httpbin.org/ip'
    proxy = p
    print("current proxy :",current_proxy," checking proxy connection of :",proxy)
    response = requests.get(url,proxies={"http": proxy, "https": proxy})

    if(response.json()!='' and current_proxy!= proxy):
        print ("Got an new proxy:",proxy)
        current_proxy=proxy
        return 'connected'
    else:
        print ("Error: ",proxy, " need another proxy")
        list_of_error_proxy.append(proxy)
        return 'error'
        

    