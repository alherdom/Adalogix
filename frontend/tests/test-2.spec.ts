import { test, expect } from '@playwright/test';

test('test', async ({ page }) => {
  await page.goto('http://localhost:9000/');
  await page.goto('http://localhost:9000/#/');
  await page.goto('http://localhost:9000/#/login');
  await page.getByLabel('Username').click();
  await page.getByLabel('Username').fill('alherdom');
  await page.getByLabel('Username').press('Tab');
  await page.getByLabel('Password').fill('1q2w3e4r');
  await page.getByRole('button', { name: 'Log in' }).click();
  await page.getByRole('heading', { name: 'Welcome Alejandro Hdez! 👋🏻' }).click();
  await expect(page.getByRole('heading')).toContainText('Adalogix');
  await page.getByRole('link', { name: 'INVENTORY' }).click();
  await expect(page.locator('#q-app')).toContainText('1-14 of 14');
});
