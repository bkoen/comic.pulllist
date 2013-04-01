#!/usr/bin/perl -w

use strict;
use warnings;
use LWP::Simple;
use File::Compare;

#################### Grab new file
getstore("http://www.previewsworld.com/shipping/newreleases.txt", "/usr/lib/cgi-bin/sand/newreleases.tmp");
###################################
########################### open both files and check to see if they match

my $neednew = 0;
my $currentpath = "/usr/lib/cgi-bin/sand/newreleases.txt";
my $newpath = "/usr/lib/cgi-bin/sand/newreleases.tmp";


open (my $current, '<', $currentpath)
or die "cant open current file";
open (my $new, '<', $newpath)
or die "cant open new file";

if (compare($current, $new) == 0){
	print "New list not availible.\n";
}
	else {
		print "New list availible, we need to replace the old list.\n";
		$neednew = 1;
}


if ($neednew == 1){
	print "lets copy that shit.\n";
	print (unlink $currentpath);
	rename $newpath, $currentpath;
}
#unlink $currentpath 
#or die "<$currentpath> not removed";
#print (unlink $currentpath);

close $current;
close $new;



