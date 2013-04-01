#!/usr/bin/perl -w
#####################################################
use strict;
use warnings;
use CGI;
use CGI::Carp qw(fatalsToBrowser);
use LWP::Simple;
#####################################################
my $q = new CGI;


###################### HTML stuff made possible by "use CGI"#################

print $q->header;
print $q->start_html("title defined in start_html");
print '<body bgcolor="grey"><font color="maroon">';


########################################################################################
############# Read newreleases.txt and store each line in @books #######################
open my $newreleases,"<", "./sand/newreleases.txt"
	or die "can not open newreleases.txt\n";

my $line;
my @books;
while ($line = <$newreleases>) 
	{
	push(@books, lc($line))
	}
close($newreleases);
#######################################################################################
########### Read wanted.txt and store each line in @pulllist ##########################
open my $wanted,"<", "./sand/wanted.txt"
	or die "can not open wanted.txt\n";
	
my $title;
my @pulllist;
while ($title = <$wanted>)
	{
	chomp($title);
	push(@pulllist, $title)
	}
close($wanted);

############## cosmetic text ###################################
print $q->h5("Be sure to pick up these books this week.<br>");
print "#################################################<br>";
################################################################
############### print each line in @books that contains a tile from @pulllist #########
my $title2;
my $fullline;
foreach $title2	(@pulllist)
{
	foreach my $i (@books)
	{
	next unless($i =~ m/$title2 (#|tp|\()/);
	print "##### $i <br>";
	}

}
#######################################################################################
############### cosmetic text #########################################################
print "#################################################<br>";

print '</font></body>';
print $q->end_html;
