# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/makeglos
# catalog-date 2007-02-23 00:16:39 +0100
# catalog-license gpl
# catalog-version undef
Name:		texlive-makeglos
Version:	20070223
Release:	8
Summary:	Include a glossary into a document
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/makeglos
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/makeglos.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/makeglos.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides the means to include a glossary into a
document. The glossary is prepared by an external program, such
as xindy or makeindex, in the same way that an index is made.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/makeglos/makeglos.sty
%doc %{_texmfdistdir}/doc/latex/makeglos/README
%doc %{_texmfdistdir}/doc/latex/makeglos/makeglos.pdf
%doc %{_texmfdistdir}/doc/latex/makeglos/makeglos.tex
%doc %{_texmfdistdir}/doc/latex/makeglos/makeglos.xdy

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20070223-2
+ Revision: 753731
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20070223-1
+ Revision: 718948
- texlive-makeglos
- texlive-makeglos
- texlive-makeglos
- texlive-makeglos

