Name:           perl-XML-Simple
Version:        2.18
Release:        0
License:        Artistic-1.0
Summary:        Easy API to read/write XML (Perl module)
Url:            http://cpan.org/modules/by-module/XML/
Group:          Development/Libraries/Perl
Source:         http://www.cpan.org/authors/id/G/GR/GRANTM/XML-Simple-%{version}.tar.gz
Source1001: 	perl-XML-Simple.manifest
BuildRequires:  perl-XML-Parser
BuildRequires:  perl-macros
Requires:       perl-XML-Parser

%description
XML::Simple - Easy API to read/write XML (esp config files)

%prep
%setup -q -n XML-Simple-%{version}
cp %{SOURCE1001} .

%build
perl Makefile.PL
make

%check
make test

%install
%perl_make_install
%perl_process_packlist

%files
%manifest %{name}.manifest
%defattr(-,root,root)
%doc %{_mandir}/man?/*
%{perl_vendorlib}/XML
%{perl_vendorarch}/auto/XML

%changelog
