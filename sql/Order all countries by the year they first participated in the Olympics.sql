select noc,min (year) from [dbo].[Order all countries by the year they first participated in the Olympics] 
group by noc
order by min (year)asc