function send_to_accury(destdir,true_labels,cluster_labels,label),
%true_labels=load('/home/zzpp220/DATA/TRAIN/lists/true_labels.lst');
%true_labels=load('/home/zzpp220/DATA/TRAIN/lists/truelabels_1260.txt');
%true_labels=load('/home/zzpp220/DATA/TRAIN/lists/truelabels_630.txt');

% destdir='/media/zzpp220/Document&&Data/Linux_Documents/9.6/624.500.13.21/';
% destfile='624.500.13.21_cluster.txt';

%cluster_labels=load(strcat(destdir,destfile));


score_acc = accuracy(true_labels, cluster_labels);
score_nmi=nmi(true_labels, cluster_labels);

%newname=strcat(destdir,'accur：',num2str(score_acc),'%_','nmi：',num2str(score_nmi*100),'%_',destfile);
newname=strcat(destdir,'accur:',num2str(score_acc),'%_','nmi:',num2str(score_nmi*100),'%_',label,'_cluster.txt');
fid=fopen(newname,'wb');

fclose(fid);