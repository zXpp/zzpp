true_labels=load('/home/zzpp220/DATA/TRAIN/lists/true_labels.lst');
%true_labels=load('/home/zzpp220/DATA/TRAIN/lists/truelabels_1260.txt');
%true_labels=load('/home/zzpp220/DATA/TRAIN/lists/truelabels_630.txt');

destdir='/media/zzpp220/Document&&Data/Linux_Documents/9.8/sparse/39.256-corresponding/shiyan/feature//';
destfile='sparse39_256_testcoor_cluster.txt';
cluster_labels=load(strcat(destdir,destfile));

score = accuracy(true_labels, cluster_labels);
newname=strcat(destdir,'accur：',num2str(score),'%_',destfile);
fid=fopen(newname,'wb');
fclose(fid);

score_nmi=nmi(true_labels, cluster_labels);
newname2=strcat(destdir,'nmi：',num2str(score_nmi*100),'%_',destfile);
fid2=fopen(newname2,'wb');
fclose(fid2);