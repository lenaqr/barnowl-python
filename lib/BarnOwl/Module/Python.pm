package BarnOwl::Module::Python;

use warnings;
use strict;
use File::Basename;
use Inline "Python" => dirname(__FILE__)."/../../../python/main.py";

init();
