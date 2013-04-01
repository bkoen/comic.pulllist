#!/usr/bin/perl -w

use strict;
use warnings;
use CGI qw(:standard);
use CGI::Carp qw(fatalsToBrowser);

#the goal of this script is to allow a user to create a wanted.txt pull list via a web browser.
my $q = new CGI;
print $q->header;
###http://www.cs.tut.fi/~jkorpela/perl/cgi.html

my $entry = $q->param('add');
chomp($entry);




########### open wanted.txt for reading ############################
open my $wanted, "<", "/var/www/wanted.txt"
or die "cant open wanted.txt for reading";
####################################################################
########## If net title ($entry) matches an existing list item, stop #####
my $i;
while  ($i = <$wanted>)
	{
		#print $i
		chomp($i);
		if ($entry eq $i)
		{
			#print "$entry is already in wanted.txt I will not add the same book twice. Stop asking";
			exit 0;
		}	
	}
###########################################################################
close $wanted;




################### open wanted.txt and append entry #########################
open my $wanted, ">>", "/var/www/wanted.txt"
or die "cant open wanted.txt";
print $wanted $entry, "\n";
close $wanted;
print $q->start_html;
#print "$entry was added to the file successfully!";
print $q->end_html;
###############################################################################


exit 0;