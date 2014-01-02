% HMM exercise  
% -------------


disp ('-------- reading signal and computing cepstra ----------');

%-----------reading in the training data----------------------------------
filepath = '../data/Training/Kinect_0.txt';
A = load(filepath)

%-------------feature extraction------------------------------------------

%fid = fopen('../data/Training/Kinect_0.txt');
%A = fscanf(fid, '%s %f %f %f', [103 inf]);
%fclose(fid);

%-------------------------------------------------------------------------

disp('')
disp('-------- training model for 1 ----------');
%-------------------------------------------------------------------------
%DONE : utiser la bonne valeur de N pour le training de vos modèles!!

N=5; A=inittran(N); [MI,SIGMA]=initemis(c1_1,N); 
[NEWA, NEWMI, NEWSIGMA, Ptot] = vit_reestim (c1_1,c1_2,c1_3, A, MI, SIGMA);
Ptot
for iter=1:5
   [NEWA,NEWMI,NEWSIGMA,Ptot] = vit_reestim (c1_1,c1_2,c1_3, NEWA, NEWMI, SIGMA);  
   Ptot
end
A1=NEWA; MI1=NEWMI; SIGMA1=SIGMA;

disp ('-------- training model for 2 ----------');
N=6; A=inittran(N); [MI,SIGMA]=initemis(c2_1,N); 
[NEWA, NEWMI, NEWSIGMA, Ptot] = vit_reestim (c2_1,c2_2,c2_3, A, MI, SIGMA);
Ptot
for iter=1:5  
   [NEWA,NEWMI,NEWSIGMA,Ptot] = vit_reestim (c2_1,c2_2,c2_3, NEWA, NEWMI, SIGMA);
   Ptot
end
A2=NEWA; MI2=NEWMI; SIGMA2=SIGMA;

disp ('-------- training model for 3 ----------');
N=8; A=inittran(N); [MI,SIGMA]=initemis(c3_1,N); 
[NEWA, NEWMI, NEWSIGMA, Ptot] = vit_reestim (c3_1,c3_2,c3_3, A, MI, SIGMA);
Ptot
for iter=1:5  
   [NEWA,NEWMI,NEWSIGMA,Ptot] = vit_reestim (c3_1,c3_2,c3_3, NEWA, NEWMI, SIGMA);  
   Ptot
end
A3=NEWA; MI3=NEWMI; SIGMA3=SIGMA;

disp ('-------- training model for 4 ----------');
N=8; A=inittran(N); [MI,SIGMA]=initemis(c4_1,N); 
[NEWA, NEWMI, NEWSIGMA, Ptot] = vit_reestim (c4_1,c4_2,c4_3, A, MI, SIGMA);
Ptot
for iter=1:5
   [NEWA,NEWMI,NEWSIGMA,Ptot] = vit_reestim (c4_1,c4_2,c4_3, NEWA, NEWMI, SIGMA);  
   Ptot
end
A4=NEWA; MI4=NEWMI; SIGMA4=SIGMA;

disp ('-------- training model for 5 ----------');
N=7; A=inittran(N); [MI,SIGMA]=initemis(c5_1,N); 
[NEWA, NEWMI, NEWSIGMA, Ptot] = vit_reestim (c5_1,c5_2,c5_3, A, MI, SIGMA);
Ptot
for iter=1:6
   [NEWA,NEWMI,NEWSIGMA,Ptot] = vit_reestim (c5_1,c5_2,c5_3, NEWA, NEWMI, SIGMA);  
   Ptot
end
A5=NEWA; MI5=NEWMI; SIGMA5=SIGMA;


disp (['====== now recognizing ' tested_person '  =======']) 
%format short e % this is to see correctly all elements of a vector

Pvit11 = viterbi_log (c1t, A1, MI1, SIGMA1);
Pvit12 = viterbi_log (c1t, A2, MI2, SIGMA2);
Pvit13 = viterbi_log (c1t, A3, MI3, SIGMA3);
Pvit14 = viterbi_log (c1t, A4, MI4, SIGMA4);
Pvit15 = viterbi_log (c1t, A5, MI5, SIGMA5);
h=[Pvit11 Pvit12 Pvit13 Pvit14 Pvit15]
[nic,ii]=max(h); disp(['testing for 1t, the best model is ' num2str(ii) ]);

Pvit11 = viterbi_log (c2t, A1, MI1, SIGMA1);
Pvit12 = viterbi_log (c2t, A2, MI2, SIGMA2);
Pvit13 = viterbi_log (c2t, A3, MI3, SIGMA3);
Pvit14 = viterbi_log (c2t, A4, MI4, SIGMA4);
Pvit15 = viterbi_log (c2t, A5, MI5, SIGMA5);
h=[Pvit11 Pvit12 Pvit13 Pvit14 Pvit15]
[nic,ii]=max(h); disp(['testing for 2t, the best model is ' num2str(ii) ]);

Pvit11 = viterbi_log (c3t, A1, MI1, SIGMA1);
Pvit12 = viterbi_log (c3t, A2, MI2, SIGMA2);
Pvit13 = viterbi_log (c3t, A3, MI3, SIGMA3);
Pvit14 = viterbi_log (c3t, A4, MI4, SIGMA4);
Pvit15 = viterbi_log (c3t, A5, MI5, SIGMA5);
h=[Pvit11 Pvit12 Pvit13 Pvit14 Pvit15]
[nic,ii]=max(h); disp(['testing for 3t, the best model is ' num2str(ii) ]);

Pvit11 = viterbi_log (c4t, A1, MI1, SIGMA1);
Pvit12 = viterbi_log (c4t, A2, MI2, SIGMA2);
Pvit13 = viterbi_log (c4t, A3, MI3, SIGMA3);
Pvit14 = viterbi_log (c4t, A4, MI4, SIGMA4);
Pvit15 = viterbi_log (c4t, A5, MI5, SIGMA5);
h=[Pvit11 Pvit12 Pvit13 Pvit14 Pvit15]
[nic,ii]=max(h); disp(['testing for 4t, the best model is ' num2str(ii) ]);

Pvit11 = viterbi_log (c5t, A1, MI1, SIGMA1);
Pvit12 = viterbi_log (c5t, A2, MI2, SIGMA2);
Pvit13 = viterbi_log (c5t, A3, MI3, SIGMA3);
Pvit14 = viterbi_log (c5t, A4, MI4, SIGMA4);
Pvit15 = viterbi_log (c5t, A5, MI5, SIGMA5);
h=[Pvit11 Pvit12 Pvit13 Pvit14 Pvit15]
[nic,ii]=max(h); disp(['testing for 5t, the best model is ' num2str(ii) ]);

disp('');
disp('');
Pvit11 = viterbi_log (cp, A1, MI1, SIGMA1);
Pvit12 = viterbi_log (cp, A2, MI2, SIGMA2);
Pvit13 = viterbi_log (cp, A3, MI3, SIGMA3);
Pvit14 = viterbi_log (cp, A4, MI4, SIGMA4);
Pvit15 = viterbi_log (cp, A5, MI5, SIGMA5);
h=[Pvit11 Pvit12 Pvit13 Pvit14 Pvit15]
[nic,ii]=max(h); disp(['testing for "peu", the best model is ' num2str(ii) ]);