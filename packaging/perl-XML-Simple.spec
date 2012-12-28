#

Name:           perl-XML-Simple
Version:        2.18
Release:        0
License:        Artistic-1.0
Summary:        Easy API to read/write XML (Perl module)
Url:            http://cpan.org/modules/by-module/XML/
Group:          Development/Libraries/Perl
Source:         http://www.cpan.org/authors/id/G/GR/GRANTM/XML-Simple-%{version}.tar.gz
BuildRequires:  perl-XML-Parser
BuildRequires:  perl-macros
Requires:       perl-XML-Parser
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{perl_requires}

%description
XML::Simple - Easy API to read/write XML (esp config files)

%prep
%setup -q -n XML-Simple-%{version}

%build
perl Makefile.PL
make

%check
make test

%install
%perl_make_install
%perl_process_packlist

%files
%defattr(-,root,root)
%doc README
%doc %{_mandir}/man?/*
%{perl_vendorlib}/XML
%{perl_vendorarch}/auto/XML

%changelog
