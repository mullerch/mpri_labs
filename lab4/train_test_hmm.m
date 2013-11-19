% HMM exercise  
% -------------



disp ('-------- reading signal and computing cepstra ----------');

%-----------reading in the training data----------------------------------
[training_data1_1, Fs1_1, bits1] = wavread('audio-samples/christian/1_1.wav');
[training_data1_2, Fs1_2, bits1] = wavread('audio-samples/christian/1_2.wav');
[training_data1_3, Fs1_3, bits1] = wavread('audio-samples/christian/1_3.wav');
[training_data2_1, Fs2_1, bits2] = wavread('audio-samples/christian/2_1.wav');
[training_data2_2, Fs2_2, bits2] = wavread('audio-samples/christian/2_2.wav');
[training_data2_3, Fs2_3, bits2] = wavread('audio-samples/christian/2_3.wav');
[training_data3_1, Fs3_1, bits3] = wavread('audio-samples/christian/3_1.wav');
[training_data3_2, Fs3_2, bits3] = wavread('audio-samples/christian/3_2.wav');
[training_data3_3, Fs3_3, bits3] = wavread('audio-samples/christian/3_3.wav');
[training_data4_1, Fs4_1, bits4] = wavread('audio-samples/christian/4_1.wav');
[training_data4_2, Fs4_2, bits4] = wavread('audio-samples/christian/4_2.wav');
[training_data4_3, Fs4_3, bits4] = wavread('audio-samples/christian/4_3.wav');
[training_data5_1, Fs5_1, bits5] = wavread('audio-samples/christian/5_1.wav');
[training_data5_2, Fs5_2, bits5] = wavread('audio-samples/christian/5_2.wav');
[training_data5_3, Fs5_3, bits5] = wavread('audio-samples/christian/5_3.wav');

[testing_data1, Fs1t, bits1t] = wavread('audio-samples/christian/1t.wav');
[testing_data2, Fs2t, bits2t] = wavread('audio-samples/christian/2t.wav');
[testing_data3, Fs3t, bits3t] = wavread('audio-samples/christian/3t.wav');
[testing_data4, Fs4t, bits4t] = wavread('audio-samples/christian/4t.wav');
[testing_data5, Fs5t, bits5t] = wavread('audio-samples/christian/5t.wav');
  
[testing_datap, Fspt, bitspt] = wavread('audio-samples/christian/peut.wav');

%-------------feature extraction, 12 coeff. ------------------------------------------
c1_1 = melcepst(training_data1_1,Fs1_1)';
c1_2 = melcepst(training_data1_2,Fs1_2)';
c1_3 = melcepst(training_data1_3,Fs1_3)';
  
c2_1 = melcepst(training_data2_1,Fs2_1)';
c2_2 = melcepst(training_data2_2,Fs2_2)';
c2_3 = melcepst(training_data2_3,Fs2_3)';
  
c3_1 = melcepst(training_data3_1,Fs3_1)';
c3_2 = melcepst(training_data3_2,Fs3_2)';
c3_3 = melcepst(training_data3_3,Fs3_3)';
  
c4_1 = melcepst(training_data4_1,Fs4_1)';
c4_2 = melcepst(training_data4_2,Fs4_2)';
c4_3 = melcepst(training_data4_3,Fs4_3)';
  
c5_1 = melcepst(training_data5_1,Fs5_1)';
c5_2 = melcepst(training_data5_2,Fs5_2)';
c5_3 = melcepst(training_data5_3,Fs5_3)';

c1t = melcepst(testing_data1,Fs1t)';
c2t = melcepst(testing_data2,Fs2t)';
c3t = melcepst(testing_data3,Fs3t)';
c4t = melcepst(testing_data4,Fs4t)';
c5t = melcepst(testing_data5,Fs5t)';

cp = melcepst(testing_datap,Fspt)';

%-------------------------------------------------------------------------
%TODO: afficher la durée des fichiers d'entraînement (en millisecondes) ainsi 
%que le nombre de vecteurs acoustiques qui en sont extraits (nombre de colonnes de la matrice ci_i)
[tmp, nb_vectors_c1_1] = size(c1_1);
[tmp, nb_vectors_c1_2] = size(c1_2);
[tmp, nb_vectors_c1_3] = size(c1_3);
[tmp, nb_vectors_c2_1] = size(c2_1);
[tmp, nb_vectors_c2_2] = size(c2_2);
[tmp, nb_vectors_c2_3] = size(c2_3);
[tmp, nb_vectors_c3_1] = size(c3_1);
[tmp, nb_vectors_c3_2] = size(c3_2);
[tmp, nb_vectors_c3_3] = size(c3_3);
[tmp, nb_vectors_c4_1] = size(c4_1);
[tmp, nb_vectors_c4_2] = size(c4_2);
[tmp, nb_vectors_c4_3] = size(c4_3);
[tmp, nb_vectors_c5_1] = size(c5_1);
[tmp, nb_vectors_c5_2] = size(c5_2);
[tmp, nb_vectors_c5_3] = size(c5_3);


[duration_c1_1, tmp2] = size(training_data1_1);
[duration_c1_2, tmp2] = size(training_data1_2);
[duration_c1_3, tmp2] = size(training_data1_3);
[duration_c2_1, tmp2] = size(training_data2_1);
[duration_c2_2, tmp2] = size(training_data2_2);
[duration_c2_3, tmp2] = size(training_data2_3);
[duration_c3_1, tmp2] = size(training_data3_1);
[duration_c3_2, tmp2] = size(training_data3_2);
[duration_c3_3, tmp2] = size(training_data3_3);
[duration_c4_1, tmp2] = size(training_data4_1);
[duration_c4_2, tmp2] = size(training_data4_2);
[duration_c4_3, tmp2] = size(training_data4_3);
[duration_c5_1, tmp2] = size(training_data5_1);
[duration_c5_2, tmp2] = size(training_data5_2);
[duration_c5_3, tmp2] = size(training_data5_3);

duration_c1_1 = duration_c1_1/Fs1_1*1000;
duration_c1_2 = duration_c1_2/Fs1_2*1000;
duration_c1_3 = duration_c1_3/Fs1_3*1000;
duration_c2_1 = duration_c2_1/Fs2_1*1000;
duration_c2_2 = duration_c2_2/Fs2_2*1000;
duration_c2_3 = duration_c2_3/Fs2_3*1000;
duration_c3_1 = duration_c3_1/Fs3_1*1000;
duration_c3_2 = duration_c3_2/Fs3_2*1000;
duration_c3_3 = duration_c3_3/Fs3_3*1000;
duration_c4_1 = duration_c4_1/Fs4_1*1000;
duration_c4_2 = duration_c4_2/Fs4_2*1000;
duration_c4_3 = duration_c4_3/Fs4_3*1000;
duration_c5_1 = duration_c5_1/Fs5_1*1000;
duration_c5_2 = duration_c5_2/Fs5_2*1000;
duration_c5_3 = duration_c5_3/Fs5_3*1000;


disp ('-------- training data overview ----------');
disp(['Sample 1_1 - ' num2str(duration_c1_1) ' msec - ' num2str(nb_vectors_c1_1) ' vectors']);
disp(['Sample 1_2 - ' num2str(duration_c1_2) ' msec - ' num2str(nb_vectors_c1_2) ' vectors']);
disp(['Sample 1_3 - ' num2str(duration_c1_3) ' msec - ' num2str(nb_vectors_c1_3) ' vectors']);
disp(['Sample 2_1 - ' num2str(duration_c2_1) ' msec - ' num2str(nb_vectors_c2_1) ' vectors']);
disp(['Sample 2_2 - ' num2str(duration_c2_2) ' msec - ' num2str(nb_vectors_c2_2) ' vectors']);
disp(['Sample 2_3 - ' num2str(duration_c2_3) ' msec - ' num2str(nb_vectors_c2_3) ' vectors']);
disp(['Sample 3_1 - ' num2str(duration_c3_1) ' msec - ' num2str(nb_vectors_c3_1) ' vectors']);
disp(['Sample 3_2 - ' num2str(duration_c3_2) ' msec - ' num2str(nb_vectors_c3_2) ' vectors']);
disp(['Sample 3_3 - ' num2str(duration_c3_3) ' msec - ' num2str(nb_vectors_c3_3) ' vectors']);
disp(['Sample 4_1 - ' num2str(duration_c4_1) ' msec - ' num2str(nb_vectors_c4_1) ' vectors']);
disp(['Sample 4_2 - ' num2str(duration_c4_2) ' msec - ' num2str(nb_vectors_c4_2) ' vectors']);
disp(['Sample 4_3 - ' num2str(duration_c4_3) ' msec - ' num2str(nb_vectors_c4_3) ' vectors']);
disp(['Sample 5_1 - ' num2str(duration_c5_1) ' msec - ' num2str(nb_vectors_c5_1) ' vectors']);
disp(['Sample 5_2 - ' num2str(duration_c5_2) ' msec - ' num2str(nb_vectors_c5_2) ' vectors']);
disp(['Sample 5_3 - ' num2str(duration_c5_3) ' msec - ' num2str(nb_vectors_c5_3) ' vectors']);

mean([duration_c1_1 duration_c1_2 duration_c1_3])
mean([nb_vectors_c1_1 nb_vectors_c1_2 nb_vectors_c1_3])

mean([duration_c2_1 duration_c2_2 duration_c2_3])
mean([nb_vectors_c2_1 nb_vectors_c2_2 nb_vectors_c2_3])

mean([duration_c3_1 duration_c3_2 duration_c3_3])
mean([nb_vectors_c3_1 nb_vectors_c3_2 nb_vectors_c3_3])

mean([duration_c4_1 duration_c4_2 duration_c4_3])
mean([nb_vectors_c4_1 nb_vectors_c4_2 nb_vectors_c4_3])

mean([duration_c5_1 duration_c5_2 duration_c5_3])
mean([nb_vectors_c5_1 nb_vectors_c5_2 nb_vectors_c5_3])


%-------------------------------------------------------------------------


disp ('-------- training model for 1 ----------');
%-------------------------------------------------------------------------
%TODO : utiser la bonne valeur de N pour le training de vos modèles!!

N=5; A=inittran(N); [MI,SIGMA]=initemis(c1_1,N); 
[NEWA, NEWMI, NEWSIGMA, Ptot] = vit_reestim (c1_1,c1_2,c1_3, A, MI, SIGMA);
Ptot
for iter=1:5
   [NEWA,NEWMI,NEWSIGMA,Ptot] = vit_reestim (c1_1,c1_2,c1_3, NEWA, NEWMI, SIGMA);  
   Ptot
end
A1=NEWA; MI1=NEWMI; SIGMA1=SIGMA;

disp ('-------- training model for 2 ----------');
N=5; A=inittran(N); [MI,SIGMA]=initemis(c2_1,N); 
[NEWA, NEWMI, NEWSIGMA, Ptot] = vit_reestim (c2_1,c2_2,c2_3, A, MI, SIGMA);
Ptot
for iter=1:5  
   [NEWA,NEWMI,NEWSIGMA,Ptot] = vit_reestim (c2_1,c2_2,c2_3, NEWA, NEWMI, SIGMA);
   Ptot
end
A2=NEWA; MI2=NEWMI; SIGMA2=SIGMA;

disp ('-------- training model for 3 ----------');
N=5; A=inittran(N); [MI,SIGMA]=initemis(c3_1,N); 
[NEWA, NEWMI, NEWSIGMA, Ptot] = vit_reestim (c3_1,c3_2,c3_3, A, MI, SIGMA);
Ptot
for iter=1:5  
   [NEWA,NEWMI,NEWSIGMA,Ptot] = vit_reestim (c3_1,c3_2,c3_3, NEWA, NEWMI, SIGMA);  
   Ptot
end
A3=NEWA; MI3=NEWMI; SIGMA3=SIGMA;

disp ('-------- training model for 4 ----------');
N=5; A=inittran(N); [MI,SIGMA]=initemis(c4_1,N); 
[NEWA, NEWMI, NEWSIGMA, Ptot] = vit_reestim (c4_1,c4_2,c4_3, A, MI, SIGMA);
Ptot
for iter=1:5
   [NEWA,NEWMI,NEWSIGMA,Ptot] = vit_reestim (c4_1,c4_2,c4_3, NEWA, NEWMI, SIGMA);  
   Ptot
end
A4=NEWA; MI4=NEWMI; SIGMA4=SIGMA;

disp ('-------- training model for 5 ----------');
N=5; A=inittran(N); [MI,SIGMA]=initemis(c5_1,N); 
[NEWA, NEWMI, NEWSIGMA, Ptot] = vit_reestim (c5_1,c5_2,c5_3, A, MI, SIGMA);
Ptot
for iter=1:5
   [NEWA,NEWMI,NEWSIGMA,Ptot] = vit_reestim (c5_1,c5_2,c5_3, NEWA, NEWMI, SIGMA);  
   Ptot
end
A5=NEWA; MI5=NEWMI; SIGMA5=SIGMA;


%disp ('====== now recognizing  =======') 
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