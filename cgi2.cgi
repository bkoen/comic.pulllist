#!/usr/bin/perl -w
#####################################################
use strict;
use warnings;
use CGI;
use CGI::Carp qw(fatalsToBrowser);
use LWP::Simple;
#####################################################
print "Content-type: text/html\n\n";

print '<html>';
print '<title>new books this week</title>';
print '<body bgcolor="grey"><font color="maroon">';

############# Read newreleases.txt and store each line in @books #######################
open my $newreleases,"<", "./newreleases.txt"
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
open my $wanted,"<", "./wanted.txt"
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
print "Be sure to pick up these books this week.<br><br>";
print "#################################################<br>";
################################################################
############### print each line in @books that contains a tile from @pulllist #########
my $title2;
my $fullline;
foreach $title2	(@pulllist)
{
	foreach my $i (@books)
	{
	next unless($i =~ m/$title2 (#|tp)/);
	print "##### $i <br>";
	}

}
#######################################################################################
############### cosmetic text #########################################################
print "#################################################<br>";

print '</font></body>';
print '</html>';
